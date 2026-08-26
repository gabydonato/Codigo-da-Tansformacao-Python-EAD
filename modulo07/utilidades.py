def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def potencializar(a, b):
    return a ** b

import utilidades

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Soma:", utilidades.soma(n1, n2))
print("Subtração:", utilidades.subtracao(n1, n2))
print("Potência:", utilidades.potencia(n1, n2))