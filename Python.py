def criar_usuario(usuarios):
    x = "USUÁRIO"
    print(x.center(60, "-"))

    cpf = input("DIGITE SEU CPF (apenas números): ")
    usuarios_lista = listar_usuario(cpf, usuarios)

    if usuarios_lista:
        print("Este usuário já existe!")
        return
    
    nome = input("DIGITE SEU NOME COMPLETO: ")
    data_nas = input("DIGITE SUA DATA DE NASCIMENTO: ")
    endereco = input("DIGITE SEU ENDEREÇO (logradouro, numero - bairro - cidade/estado): ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nas": data_nas, "endereco": endereco})

    print("USUÁRIO CRIADO!")

def listar_usuario(cpf, usuarios):
    x = "LISTAR USUÁRIOS"
    print(x.center(60, "="))
    usuarios_listados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_listados[0] if usuarios_listados else None

def criar_conta(agencia, numero_conta, usuarios):
    x = "NOVA CONTA"
    print(x.center(60, "="))
    cpf = input("DIGITE O CPF DO USUÁRIO: ")
    usuario = listar_usuario(cpf, usuarios)

    if usuario:
        print("CONTA CRIADA!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuarios}
    
    print("USUÁRIO NÃO ENCONTRADO")

def menu():
    print("1 - Depósito")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Criar Conta")
    print("5 - Listar Usuário")
    print("6 - Criar Usuário")
    print("7 - Sair")

    opcao = int(input("Digite o número da opção desejada: "))
    return opcao

def realizar_deposito(saldo, valor, extrato):
    saldo += valor
    extrato += f'Depósito: R$ {valor:.2f}\n'
    return saldo, extrato

def realizar_sacar(saldo, valor, extrato, limite, num_saques, limite_saques):
    if valor <= saldo and valor <= limite and num_saques < limite_saques:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        num_saques += 1
    else:
        print("Operação de saque inválida!")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n=============EXTRATO==============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = realizar_deposito(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato = realizar_sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_usuario(contas)

        elif opcao == 6:
            x = "NOVO USUÁRIO"
            print(x.center(60, "-"))
            criar_usuario(usuarios)

        elif opcao == 7:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Digite um dos números listados!")

main()
