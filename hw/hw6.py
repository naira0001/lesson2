def binary_search(some_list, target):
    left = 0
    right = len(some_list) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Избегаем переполнения для больших чисел

        if some_list[mid] == target:
            return mid  # Элемент найден, возвращаем индекс
        elif some_list[mid] < target:
            left = mid + 1  # Искомое число в правой половине
        else:
            right = mid - 1  # Искомое число в левой половине

    return -1  # Если элемент не найден

# Входные данные
some_list = [1, 3, 5, 7, 9, 11]
target = 3

# Вызов функции
result = binary_search(some_list, target)

# Вывод результата
if result != -1:
    print(f"Число {target} найдено на индексе {result}.")
else:
    print(f"Число {target} не найдено.")

