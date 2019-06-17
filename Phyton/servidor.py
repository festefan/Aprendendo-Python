import socket
from datetime import * 
host = '127.0.0.1'
porta = 8800


soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recebe =(host, porta)
soquete.bind(recebe)
soquete.listen(2)


print('\n Servidor Inciado ... IP: ', host, 'Prota: ', porta ,'em: ', datetime.now().strftime('%H:%M:%S'))

while True:
    conexao, enderecoIP = soquete.accept()
    print('Servidor acessado pelo Cliente: ', enderecoIP)

    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print('\n IP Cliente: ', enderecoIP)
        print('Mensagem Recebida: ', mensagem.decode(),'-',datetime.now().strftime('%H:%M:%S'))

    print('Conexão com cliente finalizada...', enderecoIP,'em: ',datetime.now().strftime('%d/%m/%a - %H:%M:%S'))
    conexao.close()
