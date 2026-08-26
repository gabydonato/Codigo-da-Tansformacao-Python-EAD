def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


numeros = [10, 5, 20, 8, 2]
resultado = maior_menor(numeros)
print(resultado)  # Saída: (20, 2)