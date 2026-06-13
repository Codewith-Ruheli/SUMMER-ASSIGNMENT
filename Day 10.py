
#to write function to check prime
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            return
        print("prime")
        num=int(input("enetr a number"))
        print(num)