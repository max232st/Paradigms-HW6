def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Искомый элемент найден, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Искомый элемент находится справа от центра
        else:
            right = mid - 1  # Искомый элемент находится слева от центра

    return -1  # Элемент не найден в массиве

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Искомый элемент {target} найден в массиве, его индекс: {result}")
else:
    print(f"Искомый элемент {target} не найден в массиве")
