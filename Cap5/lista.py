print("Exercício 1:")
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print("a) imprima o maior elemento:", max(lista))
print("b) Imprima o menor elemento:", min(lista))
print("c) Imprima números pares:", [l for l in lista if l % 2 == 0])
print("d) Imprima o número de ocorrências do primeiro elemento da lista:", lista.count(lista[0]))
print("e) Imprima a média dos elementos:", sum(lista)/len(lista))
print("f) Imprima a soma dos elementos de valor negativo:", sum([l for l in lista if l < 0]))