#!/usr/bin/env python3

import socket
import struct

s = socket.socket()
s.connect(("localhost", 6545))


s.send(b'db-client')
#bs = struct.pack("!II", 1, 0)
#s.send(bs)

magic_str = s.recv(9)
typ = struct.unpack("!I", s.recv(4))[0]
size = struct.unpack("!I", s.recv(4))[0]
reason = s.recv(size)

print("Magic str: " + str(magic_str))
print("Type: " + str(typ))
print("Size: " + str(size))
print("Reason: " + str(reason))


print("Socket should now be closed")
leftover = s.recv(1024)
print("Yepp, it is. Leftovers: " + str(leftover))
