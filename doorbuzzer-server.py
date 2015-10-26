from datetime import datetime
import argparse
import socket

__author__ = 'Emil Edholm'


def main():
    args = cmd_arguments()


    esp = ESP8266(args.password, args.host, args.port)
    status, reason = esp.unlock_door(500)


def cmd_arguments():
    parser = argparse.ArgumentParser(description='Serve the doorbuzzer')
    parser.add_argument('--host', '-i', required=True, metavar="H", help="The IP or host of the ESP8266")
    parser.add_argument('--port', '-P', required=True, type=int, metavar='P', help="The port number to connect to")
    parser.add_argument('--password', '-p', required=True, metavar='PWD', help="The password/api-key for access to the ESP8266")

    return parser.parse_args()


class SecureServer:
    def __init__(self):
        pass

    def start(self):
        pass


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
