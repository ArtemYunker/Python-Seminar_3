# 3. Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = []
new_list = []
while True:

    for i in range(5):
        list.append(float(input('Введите число  ')))
    break
print(list)

for i in range(len(list)):
    result = list[i] - int(list[i])
    new_list.append((result))

maximum = max(new_list)
minimum = min(new_list)

result = maximum - minimum
print(round(result,3))