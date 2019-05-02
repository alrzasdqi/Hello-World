#open("employees.txt", "r") #open file in read mode
#open("employees.txt", "w") #write
#open("employees.txt", "a") #append
#open("employees.txt", "r+") #read and write


employee_file = open("employees.txt", "r")
print(employee_file.readable())
#print(employee_file.read())

#print(employee_file.readline())
#print(employee_file.readline())

#print(employee_file.readlines()[1]) #gives us first line


for employee in employee_file.readlines():
	print(employee)
employee_file.close()
