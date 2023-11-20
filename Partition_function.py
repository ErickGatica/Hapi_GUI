# To compute partition funtions

from hapi import *
import matplotlib.pyplot as plt

#getHelp(partitionSum)

#partitionSum(M,I,T), where M,I - standard HITRAN molecule-isotopologue 
#notation, T - definition of temperature range.

Q=partitionSum(1,1,[70,80,90]);

T,Q1=partitionSum(1,1,[70,3000],step=1.0);
plt.plot(T,Q1)
plt.show()
