#portscan script feito com auxilio da aula

import socket
portas = [21, 23, 80, 443, 8080, 53, 25, 110, 135, 137, 138, 139, 1433, 1434, 3306, 3389, 5060, 5900, 8081, 8443, 10000]


local = input("Digite o host ou IP a ser verificado: ")

for porta in portas: 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.1)  #tempo de espera para a conexao, caso nao consiga, ele pula para a proxima porta
    resposta = cliente.connect_ex((local, porta)) # 0 Porta aberta, codigo = Porta fechada

    if resposta == 0:
        print(porta, "aberta")
    