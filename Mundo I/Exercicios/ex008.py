metro =float(input('Escreva uma distância em metros: ').strip())
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'O valor que você escreveu em metros foi {metro}')
print(f' o seu valor corresponde a {km}km,')
print(f' o seu valor corresponde a {hm}hm,')
print(f' o seu valor corresponde a {dam}dam,')
print(f' o seu valor corresponde a {dm}dm,')
print(f' o seu valor corresponde a {cm}cm,')
print(f' e o seu valor corresponde a {mm}mm.')


