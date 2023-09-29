from matplotlib import pyplot as plt
from math import pi 
import numpy as np

# make pi a x label
def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = np.int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter

x_axis = np.linspace(-pi/2, 5/2*pi, 100)
sin = np.sin(x_axis)

plt.plot(x_axis, sin)

ax = plt.gca()
ax.grid(True)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))

plt.title("Zweidimensionale Funktionen")
plt.xlabel("$y_1$")
plt.ylabel("Ordinate")
plt.show()
