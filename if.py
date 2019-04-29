x = True
y = False

if x:
	print("x is true")

if not y:
	print("'not y' is true OR y is false")

if y:
	print("y is true")
else:
	print("y is not true")

if not x:
	print("x is not true")
elif y:
	print("x is true and y is true")
else:
	print("x is true and y is false")
