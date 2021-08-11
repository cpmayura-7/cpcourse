# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 



from math import factorial
def fun_pascaltrianglevalue(row, col):
	if(row<0 or col<0):
		return None
	elif(row<col):
		return 0
	else:
		return int((factorial(row)) / ((factorial(col)) * factorial(row - col)))