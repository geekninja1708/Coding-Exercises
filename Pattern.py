#print a pattern 1->23->345-->4567
N=int(input('Enter the no. of rows'))
i=1
while i<=N:
	j=1
	while j<=i:
		for l in range(i,2*i):
		    print(l,end="")
		    j+=1
	print()
	i+=1

	
	
	
