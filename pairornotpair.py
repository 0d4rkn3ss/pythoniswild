import time

primeira_vez = True
continuar = "y"

while continuar == "y":
    entrada = input("bota aí um número: ")
    if entrada.isdigit():
        numero = int(entrada)

        if numero % 2 == 0:
            print("O número", numero, "é par")
        else:
            print("O número", numero, "é ímpar")

        while True:
            if not primeira_vez:
                continuar = input("botas outro número nabeiro? (y/n): ").lower()
            else:
                primeira_vez = False
                continuar = input("botas outro número nabeiro? (y/n): ").lower()  # Pergunta na primeira vez também

            if continuar in ("y", "n"):
                break
            else:
                print("palhaçoum do balastro, é y ou n, mete 'y' ou 'n'.")

    else:
        print("deves achar que és o pitágoras. mete só números inteiros.")

if continuar == "n":
    print("brigadão filhante, bye bye")
    time.sleep(3)
    exit()