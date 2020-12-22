import socket

ans=""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(socket.gethostname()), 12345))
ans = s.recv(1024)
print(ans)
s.close()