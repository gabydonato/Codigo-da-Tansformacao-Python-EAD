import json

clientes = {
    "Ana": "1199999-1111",
    "Bruno": "1198888-2222",
    "Carla": "1197777-3333"
}

with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)

with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)

print("Clientes cadastrados:")
for nome, telefone in dados.items():
    print(nome, "-", telefone)