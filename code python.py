from math import exp
import numpy as np

# N = 10000
# S = 0 
# for i in range (1,N):
#     S += i**(-2)
# print(S)

# def ch(x):
#     return((exp(x)+exp(-x))/2)

A = 10e3
# epsilon = 10e-1
# N = int(A/epsilon)
# integrale = 0



# for i in range (0,N):
#     integrale += 1/ch(i*epsilon)

# print (integrale)

fstring = f'une chaine formatée {2*A}'
print(fstring)

un_bool = True
un_autre_bool = not un_bool
print(un_autre_bool)

# les conteneurs 

# 2.1 les listes 

ma_liste = ['ta maman a', 45, 'strings differents']

print(ma_liste)

print(ma_liste[-1])
print(len(ma_liste))
ma_liste.append('et ils sont jolis')

une_autre_liste = ma_liste[:]
ma_liste[0] = -150
une_autre_liste[2] = 'loool'

print(ma_liste,une_autre_liste)

dico = {"key1" : "coucou", "key2" : "salut",10 : True}
print(dico["key1"])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L_2 = ['papa','maman','le ptit con']
for x  in L : 
    print (x)

for i, x in enumerate(L_2):
    print(f"{i} -> {x}")

for x,y in zip(L, L_2):
    print(f"{x}, {y}")

while x > 0.1:
    x /= 2
    print(x)

# import mes_fonctions as m

# print(m.walcalculstyle)

print(np.empty((3,5)))
