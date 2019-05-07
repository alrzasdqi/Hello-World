#working with if statements
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
#########################################################
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and  not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You either not male or not tall or both")
