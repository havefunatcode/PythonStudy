import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sname = socket.gethostname()
addr = socket.gethostbyname(sname)
print("Hostname : ", sname + "addr : ", addr)

serversocket.bind((addr, 8001))
serversocket.listen(5)

while True:
    c, caddr = serversocket.accept()
    print('Got connection from', caddr)
    print(c.recv(1024))

    msg = """HTTP/1.1 200 OK
    Content-Type: text/html
    
    
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Web Connection Example</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <h1>Please come again~</h1>
    </body>
    </html>
    
    """
    c.send(bytes(msg, "utf-8"))

    c.close()
    if input("Enter(q to quit):") == "q":
        break