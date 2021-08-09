from asyncore import dispatcher
from asyncchat import async_chat
import socket, asyncore

"""
class ChatServer(dispatcher):
    # 接続が来たときに自動で呼び出される
    def handle_accept(self):
        conn, addr = self.accept()
        print('接続要求の送信元', addr[0])

# インスタンス化
s = ChatServer()
# ソケットの作成
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
# ソケットにホストとポートを割り当てる
s.bind(('', 5005))
# サーバーを待機状態にする
s.listen(5)
asyncore.loop()
"""

PORT = 5005

class ChatSession(async_chat):
    def __init__(self, sock):
        async.chat.__init__(self, sock)
        self.set_terminater(b"\r\n")
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminater(self):
        line = b''.join(self.data)
        self.data = []
        print(line)

class ChatServer(dispatcher):
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))

if __name__ == '__main__':
    s = ChatServer(PORT)
    try:
        asyncore.loop()
    except KeyboardInterrupt: print()