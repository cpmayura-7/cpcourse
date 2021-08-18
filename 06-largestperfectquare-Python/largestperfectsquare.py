# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.
import math 
n=31
def checkPerfectSquare(n) :
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False
def largestperfectsquare(n):
    li=[]
    if(checkPerfectSquare(n)):
        return n
    else:
        for i in range(n):
            if(checkPerfectSquare(i)):
                li.append(i)
        return max(li)
print(largestperfectsquare(n))
	