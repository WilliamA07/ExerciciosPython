from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))