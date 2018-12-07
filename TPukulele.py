import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

f=441
L=0.35
d=0.6*10**(-3)
ro=1.10*10**(3)

c=2*L*f
v=((d/2)**2)*L*3.1415926535
mu=(ro*v)/L

F=c*c*mu
k=F/9.81

print(k)

X = [33, 31, 29.2, 27.5, 26, 24.6, 23.2, 21.9, 20.7, 19.5]

abss = []
ordo = []
for val in X:
    abss.append(log(c/2)-log(val))
    ordo.append(log(f)+(X.index(val)+1)/12*log(2))
    
print(abss)
print(ordo)

'''

# Data for plotting
t = abss
s = ordo

fig, ax = plt.subplots()
ax.plot(t, s,'o-')

ax.set(xlabel='ln(c/2)-ln(Ln)', ylabel='ln f + n/12 ln2',
       title='Reg linéaire')
ax.grid()

fig.savefig("test.png")
#plt.show()'''

###################

#import plotly.plotly as py
#import plotly.graph_objs as go

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

# Scientific libraries
from numpy import arange,array,ones
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(abss,ordo)
line = slope*abss+intercept

plt.plot(abss,ordo,'o', abss, line)
pylab.title('Linear Fit with Matplotlib')
ax = plt.gca()
ax.set_axis_bgcolor((0.898, 0.898, 0.898))
fig = plt.gcf()
py.plot_mpl(fig, filename='linear-Fit-with-matplotlib')
