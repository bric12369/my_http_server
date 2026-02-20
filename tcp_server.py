import socket

class TCPServer:
    def __init__(self, host='127.0.0.1', port=5678):
        self.host = host
        self.port = port

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f'Listening on {self.host}:{self.port}')
        while True:
            connection, address = server.accept()
            print(f'Connected to {address}')
            while True:
                data = connection.recv(1024)
                if not data:
                    print('Connection closed')
                    break
                print(f'Received: {data.decode()}')
                connection.sendall(b'Hello\n')
            connection.close()

tcp = TCPServer()
tcp.start()