try:
	num1 = float(input("Enter first number: "))
	# Python automatically interprets any input data as a string. To convert it to a number, you must use the float function befor input.
	op = input("Enter operator: ")
	# This is where the user enters the operation they wish to use.
	if op == "sqrt":
		print (num1 ** 0.5)
	else:
		num2 = float(input("Enter second number: "))
	# Now we need to code the operations. 
	if op == "+":
		print(num1 + num2)
	elif op == "-":
		print(num1 - num2)
	elif op == "/":
		print(num1 / num2)	
	elif op == "*":
		print(num1 * num2)
	elif op == "^":
		print(num1 ** num2)
	# But if the user gives an operation not given
except ZeroDivisionError as err:
	print(err)
except ValueError:
	print("Invalid Input Error.")

print("DONE")