opcao = 0
#vai santos
while opcao != 6:
    print("Locadora FIAP")
    print("1 - Alugar carro\n2 - Cadastras cliente")
    print("3 - Consulta carro\n4 - Análise de crédito")
    print("5 - Fale Conosco\n6 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cpf = int(input("Digite o CPF do cliente: "))
        tipo = input("Informe a categoria do carro desejado (básico, premium, luxo): ")
        print("cod: 239 BMW 2020 R$ 500,00")
        print("cod: 267 M Benz 2020 R$ 600,00")
        print("cod: 289 Audi Q3 R$ 420,00")
        cod = input("Escolha o carro desejado: ")
        dias = int(input("Quantos dias deseja alugar o carro? "))
        print(f"Você alugou uma q3 e vai pagar {dias *420}")
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        email = input("Digite o seu email: ")
        dúvida = input("Digite a sua dúvida/pergunta: ")
        print("Mais tarde entraremos em contato ou responderemos por email")
    elif opcao == 6:
        print("Obrigado por utilizar nosso sistema")
    else:
        print("Opção inválida")



