a = [1,2,3,4,5,6,7]
n1= 2
n2= 3
n3= 4

def rotLeft(a, d):
	a1= a[:d]
	a2= a[d:]
	a3=a2+a1
	return a3

print(rotLeft(a,n1))
print(rotLeft(a,n2))
print(rotLeft(a,n3))
