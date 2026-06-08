
#convert binary to decimal
n = input("Enter a binary number: ")
decimal = 0
for digit in n:
    decimal = decimal * 2 + int(digit)
print("decimal number =", decimal)