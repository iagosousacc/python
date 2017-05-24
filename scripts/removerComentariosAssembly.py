#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Feito por Iago Sousa.
# fciagsousa@gmail.com
# https://github.com/iagsousa/python/scripts

# Entrada do usuário com o nome do arquivo e
# a extensão.
f = raw_input("Insira o nome ou o caminho do arquivo: ")

# Abre o arquivo de entrada.
entrada = open(f, "r")

# Abre um arquivo chamada saida.txt para gravar
# a saida do script, se o arquivo não existir
# ele será criado.
saida = open("saida.txt", "w")

# Faz uma iteração em todas as linhas do arquivo.
for linha in entrada:
    # Quebra todas as linha existentes no arquivo onde
    # houver "//", ou seja, se houver um comentário na
    # linha atual, será criado uma lista onde o primeiro
    # elemento é todo o texto que existe antes do comentário
    # e o segundo elemento é tudo que vez depois do comentário.
    l = linha.split("//")

    # pega o texto que existe dentro do primeiro elemento da
    # nova linha, que é o texto que existe antes de qualquer
    # comentário e remove todos os espaços existentes.
    # Lembrando que se a linha não possuir comentário, o
    # a linha completa será adicionada neste elemento.
    l[0] = l[0].replace(" ", "")

    # Se o tamanho da minha lista criada pela separação
    # do comentário for maior que 1, isto quer dizer que
    # Algum comentário foi encontrado, logo o final da
    # linha seria guardado dentro da segunda parte dela
    # e assim exclui o operador de quebra de linha, então
    # apenas adicionamos ele aqui.
    if len(l) > 1:
        l[0] += "\n"

    # Este código testa se uma linha não é vazia, se
    # uma linha NÃO for vazia, então ela é adicionada
    # ao arquivo de saída
    if l[0].rstrip():
        saida.write(l[0])
