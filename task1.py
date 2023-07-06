# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def step_num(num, num2):
    steping_num = num ** num2
    return steping_num


A = int(input('Введите A: '))
B = int(input('Введите B: '))
print(f'A = {A}, B = {B} -> {step_num(A, B)}')