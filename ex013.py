salario = float(input('Qual o salário atual do funcionário? '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'.format(salario, novo))