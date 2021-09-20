import socket
import terminal

HOST = ''
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    terminal.print_name_terminal()
    conexao, cliente = tcp.accept()
    print ('Concetado por', cliente)
    while True:
        mensagem = conexao.recv(1024)
        if not mensagem: break
        print(mensagem)
    print ('Finalizando conexao do cliente', cliente)
    conexao.close()