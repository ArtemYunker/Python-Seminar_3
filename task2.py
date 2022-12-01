# 2.Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = []
new_list =[]
number = int(input('Задайте длину списка  '))

while True:
    for i in range(number):
        list.append(int(input('Введите число  ')))
    break
print(list)

for i in range((len(list)+1)//2):
    result = list[i] * list[-1-i]
    new_list.append(result)

print(new_list)