#Anuneet Anand

#Check Prime

n = int(input())
f = 0				# Number Of Factors

for i in range(1,n+1):
	if (n%i==0):
		f = f + 1

if (f==1):
	print("Neither Prime Nor Composite")
elif (f==2):
	print("Prime")
else:
	print("Composite")
