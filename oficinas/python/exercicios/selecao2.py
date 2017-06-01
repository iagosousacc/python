nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2


if media < 0:
    print("Notas inválidas!")
elif media < 4:
    print("Está reprovado!")
elif media < 7:
    print("Está de AF!")
elif media <= 10:
    print("Está aprovado!")
else:
    print("Notas inválidas!")
