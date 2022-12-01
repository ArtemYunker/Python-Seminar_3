# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число  '))
print(number)
list = []

while number > 0:
    dvoichnoe = number % 2
    number = number // 2
    list.append(dvoichnoe)

list.reverse()

print(*list)
