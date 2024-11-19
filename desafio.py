#Desafio Classificador de nível de Herói
nome = str(input("Digite seu nome: "))
xp = int(input("Digite seu XP: "))
if xp <=1000:
    print('Ferro')
elif xp >1000 and xp <2001:
    print('Bronze')
elif xp >2000 and xp <5001:
    print('Prata')
elif xp > 5000 and xp <7001:
    print('Ouro')
elif xp > 7000 and xp <8001:
    print('Platina')
elif xp > 8000 and xp <9001:
    print('Ascendente')
elif xp > 9000 and xp <10001:
    print('Imortal')
else:
    print('Radiante')
print("O Herói de nome",nome,"está no nível de", xp,"XP")
