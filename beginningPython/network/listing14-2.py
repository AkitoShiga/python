import socket

s = socket.socket()

#host = socket.gethostname()
host = "127.0.0.1"
port = 1234

s.connect((host, port))
print(str(s.recv(1024), 'utf-8'))