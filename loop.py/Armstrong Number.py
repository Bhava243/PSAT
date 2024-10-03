n = input("Enter a number: ")
l = len(n)
n = int(n)
n1 = n
res = 0
while n>0:
    rem = n % 10
    res += rem**l
    n = n//10
if res==n1:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")    
