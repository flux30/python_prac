even_gen = (num for num in range(0, 1000000, 2))

for _ in range(5):
    print(next(even_gen))