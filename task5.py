#  5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число  '))

list = []
newlist = []
perv = 1
vtor = 1

perv_1 = 1
vtor_1 = 1


for i in range(-2, number - 1):
    chislo_neg = perv - vtor
    perv = vtor
    vtor = chislo_neg
    newlist.append(chislo_neg)

for i in range(number-2):
    chislo = perv_1 + vtor_1
    perv_1 = vtor_1
    vtor_1 = chislo
    list.append(chislo)

print(list)
list3 = [1, 1]
newlist.reverse()
print(newlist + list3 + list)
