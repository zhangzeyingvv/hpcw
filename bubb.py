import matplotlib.pyplot as plt
#import collections
import numpy as np


#print bub[:,0] 
proj=['s','py','pz','px','dxy','dyz','dz2','dxz','dx2','tot']
def bubb(p,filen):
  bub=np.loadtxt(filen+'.dat',comments='k')
  x= bub[:,0] 
  y= bub[:,1]
  s= bub[:,p+2] 
  plt.scatter(x, y, s=1000*s, marker='o')
#  plt.ylim([-4,10])
  plt.ylim([-25,21])
  plt.savefig(filen+'-'+proj[p])
  plt.close()
for i in range(9):
  bubb(i,'Yb')
  bubb(i,'Pt')
  bubb(i,'Bi')
