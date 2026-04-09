from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        value = array[middle]

        if value == target:
            return middle
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1