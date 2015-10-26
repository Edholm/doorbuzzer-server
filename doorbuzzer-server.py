from datetime import datetime
import socket

__author__ = 'Emil Edholm'


def main():
    pw = ""
    host = ""
    port = 0
    esp = ESP8266(pw, host, port)
    then = datetime.now()
    status = esp.unlock_door(5000)
    now = datetime.now()
    print('OK' if status == 0 else 'NOT OK')
    print("It took: " + str((now-then).microseconds) + "ms")


class ESP8266:
    def __init__(self, password, host, port):
        self.password = password
        self.host = host
        self.port = port

    '''
    Buzz the door for the specified time.
    :param time: amount of time in milliseconds to buzz the door for
    :return: -1 if something went wrong, else 0.
    '''
    def unlock_door(self, time=1500):
        s = socket.socket()
        s.settimeout(time/1000 + 2)
        s.connect((self.host, self.port))

        msg = str.encode("{}\n{}\n".format(self.password, time))
        s.send(msg)
        ok = s.recv(6)

        if ok == b'':
            return -1

        # Wait for server to close socket.
        s.recv(1)
        return 0


if __name__ == '__main__':
    main()
