string = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

vowel_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
print("Number of vowels in the string:", vowel_count)