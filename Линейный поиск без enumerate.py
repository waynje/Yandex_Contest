def find_element_index_in_unordered_list(desired_element, unordered_list):
    """
    Находит индекс первого вхождения искомого элемента 
    в неотсортированном списке.
    """
    # Формируем цикл с количеством шагов, равным длине списка.
    for index in range(len(unordered_list)):
        # Берём элемент из списка по его индексу.
        if unordered_list[index] == desired_element:
            return index
    return None