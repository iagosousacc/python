def somaTudo(numero):
    soma = 0
    for i in range(1, numero+1):
        soma += i
    return soma

# Código Principal
num = int(input("Informe o número: "))
print ("A soma total é %d" % somaTudo(num))
