import numpy as np

N=int(input('Enter the no. of bulidings'))
w= [int(w) for w in input("Enter all the building's HEIGHT value: ").split(',')]
l=[int(l) for l in input("Enter all the building's WIDTH value: ").split(',')]
Total_length= sum(l)
Height=min(w)
Area_max=Total_length*Height
print(Area_max)
 master
	
