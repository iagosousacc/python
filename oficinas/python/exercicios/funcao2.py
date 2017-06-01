def multiplica(lista, numero):
    for i in range(len(lista)):
        lista[i] *= numero

numeros = [12,45,32,120,54,10,56,32]
for i in numeros:
    print (i,end = " ")
print ("\n")

n = int(input("Informe o numero: "))
multiplica(numeros, n)

for i in numeros:
    print (i,end = " ")
print ("\n")
