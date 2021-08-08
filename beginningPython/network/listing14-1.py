import socket

# ソケットオブジェクトをインスタンス化
s = socket.socket()

#host = socket.gethostname()
host = "127.0.0.1"
port = 1234

# ソケットオブジェクトにホストとポートをバインドする
s.bind((host, port))
print(str(host))

# ここの引数がよくわからん
s.listen(1)
while True:
    c, addr = s.accept()
    print('Connection: ', addr)
    c.send(bytes('Thanks for Connection', 'utf-8'))
    c.close()
