#operador E and
#saldo >= saque and saque <= limite
#operador OU or
#saldo >= saque or saque <= limite
#operador NAO not
#not saldo > limite
print(True and True)
print(True and False)
print(False and False)
print(False or False)
print(True or True)
print(True or False)


saldo = 1000
saque = 250
limite = 200
conta_especial = True



saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
