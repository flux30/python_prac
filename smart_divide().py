def smart_divide(func):
    def inner(a, b):
        try:
            result = func(a, b)
        except ZeroDivisionError:
            print("Error: Division by zero!")
            result = None
        return result
    return inner

@smart_divide
def divide(a, b):
    return a / b
result1 = divide(10, 2)
print("Result1:", result1)

result2 = divide(5, 0)
print("Result2:", result2)  