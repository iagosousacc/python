lista = []
num = int(input("Informe um número: "))
while num != 0:
    lista.append(num)
    num = int(input("Informe um número: "))

produto = 1
for i in lista:
    print(i, end = " ")
    produto *= i

print("\nO resultado do produto é %d" % produto)
