
# def elimination(arr):
#     seen = set()
#     for num in arr:
#         if num in seen:
#             return num
#         else:
#             seen.add(num)
#     return None

# чье-то красивое решение:
def elimination(arr):
    for x in arr:
        if arr.count(x) == 2:
            return x

print(elimination([2, 5, 34, 1, 22, 1]))
print(elimination([2, 2, 34, 1, 22]))
print(elimination([2, 5, 34, 1, 22]))
