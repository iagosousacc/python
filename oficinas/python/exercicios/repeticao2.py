num = int(input("Informe o número: "))

fatorial = 1

if num < 0:
    print("Numero inválido!")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    for i in range(2, num+1):
        fatorial *= i
    print("O fatorial de %d é %d" % (num, fatorial))
