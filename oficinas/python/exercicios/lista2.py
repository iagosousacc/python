nomes = []
idades = []
for i in range(5):
    nomes.append(input("Informe o nome: "))

for i in range(5):
    idades.append(int(input("Informe a idade: ")))

for i in range(len(nomes)):
    print("Nome: %s\nIdade: %d" % (nomes[i], idades[i]), end = "\n\n")
