import socket

My_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
My_Sock.connect(('data.pr4e.org', 80))
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
My_Sock.send(cmd)

while True:
    data = My_Sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
My_Sock.close()
