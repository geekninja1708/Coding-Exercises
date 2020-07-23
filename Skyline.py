import numpy as np
from math import *

N=int(input('Enter the no. of bulidings'))
w= [int(w) for w in input("Enter all the building's HEIGHT value: ").split(',')]
l=[int(l) for l in input("Enter all the building's WIDTH value: ").split(',')]


total_length=sum(l)
height=min(w)
Area_max=total_length*height
print(Area_max)

	
