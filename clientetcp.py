import socket

SERVER = '127.0.0.1'
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)

tcp.connect(dest)

print("Para siar use o CTRL+X\n")
mensagem = input()

while mensagem != '\x18':
    tcp.send(mensagem.encode())
    mensagem = input()

tcp.close()
