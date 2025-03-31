import time

while True:
    print("Escolha o número da questão (1 a 5) ou digite 'e' para sair:")
    escolha = input("Meta a sua escolha: ")

    if escolha.lower() == 'e':
        print("Boa atão, até logo!")
        break

    if not escolha.isdigit() or not (1 <= int(escolha) <= 5):
        print("Escolha inválida. Por favor, escolha um número entre 1 e 5 ou 'e' "
              "para sair.")
        continue

    numero_questao = int(escolha)

    if numero_questao == 1:
        print("Questão 1: Declare uma variável chamada idade e atribua um valor "
              "inteiro.")
        time.sleep(2)
        idade = 25
        print(f"A sua idade é: {idade}")
    elif numero_questao == 2:
        print("Questão 2: Escreva um código em Python que verifique se um número "
              "armazenado em uma variável chamada número é par ou ímpar.")
        print("Verifique também o script 'pairornotpair.py' neste repositório!")
        time.sleep(2)
        numero = 7
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    elif numero_questao == 3:
        print("Questão 3: Escreva um código em Python que imprima os números de 1 "
              "a 10 utilizando um loop for.")
        time.sleep(2)
        for i in range(1, 11):
            print(i)
    elif numero_questao == 4:
        print("Questão 4: Crie uma função chamada soma que receba dois números como "
              "parâmetros e retorne a soma deles. Em seguida, chame a função e "
              "imprima o resultado.")
        time.sleep(2)
        def soma(a, b):
            return a + b
        resultado = soma(10, 20)
        print(f"O resultado da soma é: {resultado}")
    elif numero_questao == 5:
        print("Questão 5: Escreva um código em Python que armazene uma string em "
              "uma variável chamada mensagem e imprima a quantidade de caracteres "
              "dessa string.")
        time.sleep(2)
        mensagem = ("Python é uma linguagem de programação poderosa. No entanto, "
                    "bananas são mais lendárias!")
        print(f"A mensagem é: '{mensagem}'")
        print(f"A quantidade de caracteres na mensagem é: {len(mensagem)}")

    time.sleep(1)