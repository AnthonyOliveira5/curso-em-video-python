v = float(input('Qual o preço do produto? R$ '))
p = v * 0.05
np = v - p
print(f' O produto custa R$ {v:.2f}, e com o desconto de 5% ele passa a custar R$ {np:.2f}.')
#pode ser feito também novo preço = v - (v * 5 / 100)
