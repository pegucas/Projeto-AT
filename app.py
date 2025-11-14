import random

print("Bem vindo ao joguinho em python da Pudin.tech")

querer = input("Vamos começar então? s/n: ")
if querer == 's':

    numero = random.randint(1, 100)

    def desci():
        
        descobrir = int(input("Coloque o numero: "))

        if descobrir == numero:
            print('Voce acertou seu numero era:')
            print(numero)
        elif descobrir > numero:
            print("Seu palpite é maior")
            desci()
        elif descobrir < numero:
            print("Seu palpite é menor")
            desci()
    desci()
else:
    print("Desitiu")
