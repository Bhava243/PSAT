a = input("Enter a string: ")

len_str = len(a)
temp = ''
for i in range(len_str-1,-1,-1):
    temp = temp + a[i]
    print(temp)

if a == (a[::-1]):
    print("Palindrome")
else:
    print("Not a Palindrome")    