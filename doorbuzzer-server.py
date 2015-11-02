from datetime import datetime
import argparse
import socket
import signal
import struct

__author__ = 'Emil Edholm'

CLIENT_MAGIC_STR = b'db-client'
SERVER_MAGIC_STR = b'db-server'

def main():
    args = cmd_arguments()
    esp = ESP8266(args.password, args.host, args.port)
    ss = SecureServer(esp)

    signal.signal(signal.SIGINT, ss.handle_sigint)

    ss.start()



def cmd_arguments():
    parser = argparse.ArgumentParser(description='Serve the doorbuzzer')
    parser.add_argument('--host', '-i', required=True, metavar="H", help="The IP or host of the ESP8266")
    parser.add_argument('--port', '-P', required=True, type=int, metavar='P', help="The port number to connect to")
    parser.add_argument('--password', '-p', required=True, metavar='PWD', help="The password/api-key for access to the ESP8266")

    return parser.parse_args()


class SecureServer:
    def __init__(self, esp):
        self.esp = esp
        self.types = {
                'error': struct.pack("!I", 1),
                'ok': struct.pack("!I", 0),
            }

    ''' Start serving clients.
        Types: 0: reserved
               1: unlock
    '''
    def start(self):
        self.s = socket.socket()
        try:
            self.s.bind(("0.0.0.0", 6545))
        except socket.error as e:
            print("Unable to bind: " + str(e))
            return

        # Allow two connections before refusing
        self.s.listen(2)

        while True:
            client, addr = self.s.accept()
            print("Connection from " + addr[0])
            self.handle_client(client)

        self.s.close()

    def close(self):
        self.s.close()

    def handle_sigint(self, signum, frame):
        print("Caught SIGINT")
        self.close()
        import sys
        sys.exit(0)

    def handle_client(self, client):
        magic_str = client.recv(len(CLIENT_MAGIC_STR))
        msg_type = struct.unpack("!I", client.recv(4))[0]
        time = struct.unpack("!I", client.recv(4))[0]

        if magic_str != CLIENT_MAGIC_STR:
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            return

        if msg_type != 1:
            client.send(SERVER_MAGIC_STR)
            client.send(self.types['error'])

            err_str = b'Unsupported operation'
            client.send(struct.pack("!I", len(err_str)))
            client.send(err_str)
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            return

        status, reason = self.esp.unlock_door(time)
        reason_bytes = str.encode(reason)
        client.send(SERVER_MAGIC_STR)
        typ = self.types['ok'] if status else self.types['error']
        client.send(typ)
        client.send(struct.pack("!I", len(reason_bytes)))
        client.send(reason_bytes)

        client.shutdown(socket.SHUT_RDWR)
        client.close()


class ESP8266:
    def __init__(self, password, host, port):
        self.password = password
        self.host = host
        self.port = port

    '''
    Buzz the door for the specified time.
    :param time: amount of time in milliseconds to buzz the door for
    :return: (False, reason) if something went wrong, else true.
    '''
    def unlock_door(self, time=1500):
        s = socket.socket()
        s.settimeout(time/1000 + 2)
        try:
            s.connect((self.host, self.port))
        except Exception as e:
            return False, str(e)

        msg = str.encode("{}\n{}\n".format(self.password, time))
        s.send(msg)
        ok = b''
        try:
            ok = s.recv(1024)
        except:
            return False, "ESP8266 probably crashed..."

        if ok == b'':
            return False, "Wrong password?"

        # Wait for server to close socket.
        try:
            s.recv(1024)
        except:
            return False, "ESP8266 probably crashed..."

        if ok == b'opened\n':
            return True, 'Everything went better than expected'
        return False, 'Unknown error'

if __name__ == '__main__':
    main()
