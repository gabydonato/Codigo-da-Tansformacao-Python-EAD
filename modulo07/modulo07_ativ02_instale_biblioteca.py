from datetime import datetime

agora = datetime.now()

print("Data e hora atuais:")
print(agora.strftime("%d/%m/%Y %H:%M:%S"))

ano = int(input("Digite seu ano de nascimento: "))
idade = agora.year - ano

print("Você tem", idade, "anos.")