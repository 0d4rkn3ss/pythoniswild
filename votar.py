import time

while True:
    try:
        age = float(input("mete aí a tua idade: "))
        if age != int(age):
            print("já agora mete só números inteiros, não vale a pena tentares enganar o sistema")
        elif age > 100:
            print("daqui a bocado és mais velho que o próprio tempo, mete uma idade válida")
        else:
            age = int(age)
            break
    except ValueError:
        print("és memo burro, mete só números inteiros, não é assim tão difícil")

if age >= 16:
    print("podes votar paspalhoum")
else:
    print("espera aí, não podes votar, ainda não tens idade para isso")
time.sleep(2)