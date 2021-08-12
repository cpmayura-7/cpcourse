# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	if(m1==m2 or (b1-b2)/(m1-m2)==1 or (b1-b2)/(m1-m2)==-1):
		return None
	elif(m1 or m2):
		return int(-(b1-b2)/(m1-m2))
	
