x = ['a','b', 'c','d']
# slicing
x1 = x[1:3]
print(x1)

print(x[1])
print(x[3])

print(len(x))

li = [1,2,'Hi',2.3]
print(li)

marks = []
marks.append(5)
marks.append(4)
marks.append(6)
marks.append((7,4))
marks.append('1')
marks.append([8,9])
new_marks=marks
marks.reverse()
print(marks)

days = []
for i in range(4):
    days.append(i)
print(days)    
days.insert(2,6)
days.insert(0,2)
print(days) 
days.remove(6)
print(days) 

# sets will not allow duplicates
s={1,2,3,2,3,4,}
print(s)

# key values
d = {'roll': 11, 'name':'Bhava'}
print(d['roll'], d['name'])

d = {'roll': 11, 'name':'Bhava',0:'First dict'}
print(d[0])

