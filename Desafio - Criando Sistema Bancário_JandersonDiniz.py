# Criando Sistema Bancário - Desafio DIO_NTT Data
#Autor: Janderson Diniz
#https://github.com/Jandersondiniz/Data-Enginer-com-Python---NTT-Data_DIO.git

def depositar(saldo, extrato): #defini a função depositar
    valor = input("Informe o valor do depósito: ")
    try:
        valor = float(valor)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado não é numérico.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite): #defini a função sacar
    valor = input("Informe o valor do saque: ")
    try:
        valor = float(valor)
        if valor > saldo:
            print(f"Operação falhou! Saldo insuficiente. Saldo atual: R$ {saldo:.2f}")
        elif valor > limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Operação falhou! Número máximo de {LIMITE_SAQUES} saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado não é numérico.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato): #defini a função exibir extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main(): #defini a função menu, onde o usuário escolhe a opção desejada
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
