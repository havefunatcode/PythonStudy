import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.gethostbyname(socket.gethostname())
port = 12345
print("Svr Addr : " + addr, "port : ", port)

s.bind((addr, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()