a=10
b=15
c=20

pi=3.14

cond=True
op_cond=False

message1 = 'welcome to "python world"'
message2 = "welcome to 'python world'"
message3 = """welcome to 'python world'
and again welcome to "python world"!"""

print("a=",a)
print("b=",b)
print("c=",c)
print("pi=",pi)
print("cond=",cond)
print("op_cond=",op_cond)

print(type(a))

print("a+b=",a+b)
print("c/a=",c/a)

print("circle=",pi*c*c)

print(message1)
print(message2)
print(message3)

print("a>b is ",a>b)
print("but a<b is ",a<b)

print("True and False means: ",cond and op_cond)
print("True OR False means: ",cond or op_cond)

#############################

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = float(num1) + float(num2) #use float function instead of int
print(result)
