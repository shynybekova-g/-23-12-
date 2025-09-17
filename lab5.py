lst = [1, 2, 3, 4, 5]
print(lst[::-1])

def list_sort(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)

numbers = [3, -7, 2, -9, 0, 5]
print(list_sort(numbers))

def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

nums = [10, 20, 30, 40]
print(change(nums))