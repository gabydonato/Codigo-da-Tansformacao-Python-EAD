import csv

with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])

    for i in range(3):
        nome = input("Nome do aluno: ")
        nota = float(input("Nota do aluno: "))
        escritor.writerow([nome, nota])

print("\nNotas cadastradas:")

with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)