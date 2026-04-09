salario_antigo= float(input("DIGITE SEU ANTIGO SALARIO! "))
porcentagem = float(input("DIGITE A PORCENTAGEM DO AUMENTO DO SALARIO! "))
salario_novo = salario_antigo*porcentagem/100+salario_antigo
Aumento = salario_novo - salario_antigo
print (f" Seu Salário era de R${salario_antigo}, antes do aumento de {porcentagem}%, você teve um aumento de R${Aumento} no seu salário e seu novo salário é de R${salario_novo}")
