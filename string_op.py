string = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
whitespace_count = 0

for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        whitespace_count += 1

print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
print("Number of digits:", digit_count)
print("Number of whitespace characters:", whitespace_count)