arquivo = open("informacoes.txt", "w")

arquivo.write("Nome: Maria\n")
arquivo.write("Idade: 15 anos\n")
arquivo.write("Cidade: São Paulo\n")

arquivo.close()

arquivo = open("informacoes.txt", "r")

conteudo = arquivo.read()
print(conteudo)

arquivo.close()