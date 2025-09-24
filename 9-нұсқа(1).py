x = [10, 15, 22, 35, 50, 7, 5, 100, 12, 30, 45, 60, 13, 25, 40]
for i, num in enumerate(x, start=1):
    if num % 5 == 0:
        print(f"{i}-элемент ({num}) 5-ке бөлінеді")
    else:
        print(f"{i}-элемент ({num}) 5-ке бөлінбейді")