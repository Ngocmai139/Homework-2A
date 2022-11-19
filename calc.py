
import re
#define the function called calculator, and it contains equation
def calculator(equation):
	print("python test.py")
	# Expression evaluation in String
	# Using regex + map() + sum()
	equation = sum(map(int, re.findall(r'[+-]?\d+',calculator)))
 
  


