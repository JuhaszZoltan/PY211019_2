import random

# szam = 1000
# while szam > 100:
#     szam = random.randint(0, 1000)
#     if szam <= 100: break
#     print(szam)
# else:
#     print('most futott le az else')

# print('ez pedig a while után fut le')

pin = 1234
proba = 3

while pin != int(input('add meg a PIN kódot: ')):
    proba -= 1
    if proba == 0: 
        print('elfogytak a lehetőségek :(')
        break
else: print('sikeresen beléptél')

# a while ciklusnak lehet 'else' ága CSAK a PYTHONBAN(!!!):
# ez akkor fut le, ha a while törzsén belül
# soha nem futott le 'break' utasítás
print('ide')



