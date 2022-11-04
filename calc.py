def calculator(number1,number2,operator):	#create the fucntion call calculator
if operator=="+": 				# if operator is "+",then we do addition 
print(float(number1)+ float(number2))
elif operator=="-":				# else if operator is "-",then we do subtraction
print(float(number1)-float(number2))
elif operator=="*":				# else if operator is "*",then we do multiplication
print(float(number1)*float(number2))		
elif operator=="/":				# else if operator is "/",then we do division 
print(float(number1)/float(number2))
elif operator=="//":				# else if operator is "//",then we do perform integer division
print(float(number1)//float(number2))
elif operator=="**":				# else if operator is "**",then we do power operation
print(float(number1)**float(number2))
else:
return False					# else return False


