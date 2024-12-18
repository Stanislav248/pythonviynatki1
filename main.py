# Завдання 1
"""
name = str(input("Привіт! Введить своє імя: "))
age = int(input("Тепер вік: "))

if age >= 120:
    print ("Помилка")
elif age <= 0:
    print("Помилка")
else:
    print("Привіт ", {name}, "!")
"""
# Завдання 2. Перша версія
"""
def user(name, age):
    if age < 0 or age > 130:
        raise ValueError("Некоректний вік.")
    return f"Привіт, {name}! Твій вік — {age}"

try:
    name = input("Введіть своє ім'я: ")
    age = int(input("Введіть свій вік: "))
    print(user(name, age))
except ValueError as e:
    print(f"Помилка: {e}")
"""
# Завдання 2. Друга версія
"""
def user(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Некоректний вік.")
        return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as e:
        return f"Помилка: {e}"

name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))
print(user(name, age))
"""
# Завдання 3
"""
try:
    numbers= []
    while True:
        num = int(input("Введіть число (або 0 для завершення): "))
        if num == 0:
            break
        if num < 0:
            raise ValueError("Знайдено від'ємне значення ")
        numbers.append(num)
    print(f"Сума всіх чисел: {sum(numbers)}")
except ValueError as e:
    print(f"Помилка: {e}")
"""
# Завдання 4. Перша версія
"""
def userfunction(numbers):
    if any(num < 0 for num in numbers):
        raise ValueError("Список містить від'ємні значення ")
    return sum(numbers)

try:
    numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
    print(f"Сума чисел: {userfunction(numbers)}")
except ValueError as e:
    print(f"Помилка: {e}")
"""
# Завдання 4. Друга версія
"""
def userfunction(numbers):
    try:
        if any(num < 0 for num in numbers):
            raise ValueError("Список містить від'ємні значення.")
        return sum(numbers)
    except ValueError as e:
        return f"Помилка: {e}"

numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
print(userfunction(numbers))
"""

