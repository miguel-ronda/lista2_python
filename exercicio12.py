#escreva um progrsms que pergunte o valor total da conta em seguida pergunte quantos clientes existem,divida a conta pelos clientes e exiba o quANTO cada cliente deve pagar,seguido da mensagem" cada cleinte deve pagar :"valor x" 
conta = int(input("valor da conta"))
clientes = int(input("quantos clientes"))
pagamento = conta/clientes 
print("cada cliente deve pagar",pagamento)