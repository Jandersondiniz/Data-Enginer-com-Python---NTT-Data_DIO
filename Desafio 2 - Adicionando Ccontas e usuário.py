import textwrap

def mostrar_menu():
    """Exibe o menu de opções para o usuário."""
    opcoes_menu = """
    ================ MENU ================
    [d] Depósito
    [s] Saque
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    => """
    return input(textwrap.dedent(opcoes_menu))

def realizar_deposito(saldo_atual, valor_deposito, historico_extrato):
    """Realiza a operação de depósito na conta bancária."""
    if valor_deposito > 0:
        saldo_atual += valor_deposito
        historico_extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação inválida! O valor do depósito deve ser positivo.")
    
    return saldo_atual, historico_extrato

def realizar_saque(saldo_atual, valor_saque, historico_extrato, limite_saque, saques_realizados, max_saques_diarios):
    """Realiza a operação de saque com as devidas validações."""
    saldo_insuficiente = valor_saque > saldo_atual
    saque_acima_limite = valor_saque > limite_saque
    limite_saques_excedido = saques_realizados >= max_saques_diarios

    if saldo_insuficiente:
        print("\nSaldo insuficiente para o saque.")
    elif saque_acima_limite:
        print("\nO valor do saque excede o limite permitido.")
    elif limite_saques_excedido:
        print("\nVocê atingiu o limite máximo de saques diários.")
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        historico_extrato += f"Saque: R$ {valor_saque:.2f}\n"
        saques_realizados += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação inválida! O valor do saque deve ser positivo.")
    
    return saldo_atual, historico_extrato, saques_realizados

def exibir_extrato(saldo_atual, historico_extrato):
    """Exibe o extrato bancário com todas as movimentações e saldo atual."""
    print("\n=============== EXTRATO ===============")
    if historico_extrato:
        print(historico_extrato)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")
    print("========================================")

def cadastrar_usuario(lista_usuarios):
    """Cadastra um novo usuário verificando duplicidade de CPF."""
    cpf = input("Digite o CPF (apenas números): ")
    usuario_existente = buscar_usuario_por_cpf(cpf, lista_usuarios)

    if usuario_existente:
        print("\nJá existe um usuário com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    lista_usuarios.append(novo_usuario)
    print("\nUsuário cadastrado com sucesso!")

def buscar_usuario_por_cpf(cpf, lista_usuarios):
    """Busca um usuário na lista de usuários pelo CPF."""
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta_bancaria(agencia, numero_conta, lista_usuarios):
    """Cria uma nova conta bancária associada a um usuário existente."""
    cpf = input("Informe o CPF do titular: ")
    usuario = buscar_usuario_por_cpf(cpf, lista_usuarios)

    if usuario:
        nova_conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "titular": usuario
        }
        print("\nConta criada com sucesso!")
        return nova_conta
    
    print("\nUsuário não encontrado. Não foi possível criar a conta.")
    return None

def listar_todas_contas(lista_contas):
    """Exibe todas as contas bancárias cadastradas no sistema."""
    if not lista_contas:
        print("\nNenhuma conta cadastrada.")
    for conta in lista_contas:
        print("=" * 50)
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['titular']['nome']}")

def main():
    """Função principal que gerencia o fluxo do sistema bancário."""
    LIMITE_SAQUES = 3
    AGENCIA_PADRAO = "0001"

    saldo = 0
    limite_saque = 500
    extrato = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, saques_realizados = realizar_saque(saldo, valor, extrato, limite_saque, saques_realizados, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            nova_conta = criar_conta_bancaria(AGENCIA_PADRAO, numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)

        elif opcao == "lc":
            listar_todas_contas(contas)

        elif opcao == "q":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
