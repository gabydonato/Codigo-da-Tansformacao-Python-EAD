aluno = {
    "nome": "Lucas Silva",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")

media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média: {media:.2f}")