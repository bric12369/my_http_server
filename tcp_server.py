import socket

HOST = '127.0.0.1'
PORT = 5678

def TCPServer(HOST, PORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f'Listening on {HOST}:{PORT}')
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

TCPServer(HOST, PORT)