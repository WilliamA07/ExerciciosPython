real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dólar = real / 4.88
euro = real / 5.38
print('Com R${:.2f}, você terá US${:.2f} '.format(real, dólar))
print('Com R${:.2f}, você terá €{:.2f}'.format(real, euro))
