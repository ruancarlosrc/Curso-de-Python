nome = "Gorbachov"
idade = "48"
profissao = "Programdor"
linguagens = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28, "saldo": 42.435}

print("Nome: {} Idade: {}".format(nome, idade,))
print("Nome: {nome} Idade: {idade}".format(idade=idade, nome=nome,))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")
