total_num = int(input("\nEnter a number: "))
sum_of_numbers = 0
for i in range (total_num):
    num= int(input("\nEnter number: "))
    sum_of_numbers += num
avg = sum_of_numbers/total_num
print(f"\nThe average of the numbers is: {avg}")