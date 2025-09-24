A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
product = 1
for i in range(4):
    for j in range(i):
        product *= A[i][j]
print("Басты диагональ астындағы элементтердің көбейтіндісі:", product)