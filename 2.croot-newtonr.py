#Nadish Shajahan
#Program to find the cube root of a number using Newton-Raphson method.
#https://github.com/nadishs/
n = input()

guess = n
count = 0
eps = 0.000001

while abs(guess**3-n)>eps:
	guess=guess-(guess**3-n)/(3.0*(guess**2))
	count = count + 1

print "Cube Root of ",n ," : ", guess, " in Time: ",count
