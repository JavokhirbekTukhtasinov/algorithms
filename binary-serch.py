arr = [1, 2, 3, 4, 5, 6, 7, 8, 12, 12, 13, 14]


# def search(target, arr):
#     letf = 0
#     right = len(arr) - 1
#     while letf <= right:
#         mid = (letf + right) // 2
#         if target == arr[mid]:
#             return mid
#         elif target > arr[mid]:
#             letf = mid + 1
#         else:
#             right = mid - 1
#     return -1


# print(search(8, arr))

def binary(target: int, arr: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary(12, arr))
