num = int(input("Enter a number to reverse: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num//=10 #returns the integer part of the result

print("Reversed number:", reversed_num)