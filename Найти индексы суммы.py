def find_sum_pair(number, sorted_list):
    left = 0
    right = len(sorted_list) - 1

    while left < right:
        current_sum = sorted_list[left] + sorted_list[right]
        if current_sum == number:
            return (left, right)
        elif current_sum < number:
            left += 1
        else:
            right -= 1
    
    return None

# Пример использования функции:
number = 10
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair = find_sum_pair(number, sorted_list)
if pair is not None:
    print(f"Найдена пара сумма которых равна {number}: {sorted_list[pair[0]]} (индекс {pair[0]}) и {sorted_list[pair[1]]} (индекс {pair[1]})")
else:
    print(f"Для числа {number} не найдено пары элементов в списке.")