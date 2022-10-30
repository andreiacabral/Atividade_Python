print('-='*20)
print('Analisador de Triangulos')
print('-='*20)

a=float(input('Base: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triangulo!')
    area=((a*b)/2)
    print('A area do triangulo é:', area)
else:
    print('Os segmentos acima não pode formar triangulo')
