#To print prime number in a range
start = int(input("enter a number:"))
end = int(input("enter a number:"))

print("prime numbers are:")
for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if(num%i) ==0:
                break
            else:
                print(num)


        
