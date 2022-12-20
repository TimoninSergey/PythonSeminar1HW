"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

def true_check(x, y, z):
    print(not(x or y or z) == (not x and not y and not z))  #Толком не понял задачи, поэтому просто сделал буквально.

X = int(input('Введите X: '))
Y = int(input('Введите Y: '))
Z = int(input('Введите Z: '))

true_check(X,Y,Z)