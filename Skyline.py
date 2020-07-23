import numpy as np

N=int(input('Enter the no. of bulidings'))
w= [int(w) for w in input("Enter all the building's width value: ").split()]
l=[int(l) for l in input("Enter all the building's length value: ").split()]

total_length_1=sum(l)
height_1=min(w)
total_length_2=sum(w)
height_2=min(l)
Area=[]
Area.append(total_length_1*height_1)
Area.append(total_length_2*height_2)
print(max(Area))
	
