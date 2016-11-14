#Nadish Shajahan
#Program to find the cube root of a number using bisection method.
#https://github.com/nadishs/
n = input()

high = n
low = 0
eps = 0.0000001
count = 0 # no of steps
mid = (low + high) / 2.0

while abs((mid**3)-n) > eps :

	if mid**3 < n:
		low = mid
	else:
		high = mid
	mid = (low + high)/2.0
	count = count + 1

guess = mid
print "Cube Root of ",n ," : ", guess, " in Time: ",count
