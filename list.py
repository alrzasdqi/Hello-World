a=2
numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(10)
numbers.remove(a)
numbers.pop(-3)
numbers.pop(0)
b=numbers.index(5)
print("b is: ",b)
numbers.reverse()
numbers.sort()
for i in numbers:
	print(i)
count=numbers.count(6)
print("no.6 count is: ",count)

##################################################

#store lists of information

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[1:3])
