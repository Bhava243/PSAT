n = int(input("Enter a number: "))
result = 0
n1 = n
while n>0:
    rem = n%10
    result = result*10 + rem
    n = n//10
if result==n1:
    print("palindrome")
else:
    print("not a palindrome")
