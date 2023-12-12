from math import sin
import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as sci

voltage_max=2     #V
frequency=1       #Hz
RESITOR=20        #Ohm
COIL=9e-3         #H
CAPACITOR=1000e-6  #   F

TOTALTIME=2       #Seconds
TIMESTEP=1e-3     #Seconds
time=np.linspace(0, TOTALTIME, int(TOTALTIME/TIMESTEP)+1)

A=np.array([[-1/(RESITOR*CAPACITOR),    -1/CAPACITOR], 
            [1/COIL,                    0]])
B=np.array([[1/(RESITOR*CAPACITOR)],
            [0]])
C=np.array([[1,             0],
            [0,             1],
            [-1/RESITOR,    0]])
D=np.array([[0],
            [0],
            [1/RESITOR]])

def xdot_fkt(t, x):
    x=np.reshape(x, (2,1))
    u_e = voltage_max * sin(2*np.pi*frequency*t)
    xdot = A.dot(x) + B * u_e
    xdot=np.reshape(xdot, (1,2))
    return xdot

u_a_0=0; i_l_0=0  # Anfangswerte
x0=np.array([u_a_0, i_l_0])

sol = sci.solve_ivp(xdot_fkt, [0, TOTALTIME], x0, t_eval=time, method='LSODA')
x=sol.y;
u_e = voltage_max * np.sin(2*np.pi*frequency*time)
y = C.dot(x) + D * u_e
u_a=y[0]
i_c=y[2]-y[1]
i_e=y[2]

fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(211)
ax.plot(time, u_a, 'black')
ax.plot(time, i_c, 'r')
ax.grid()
ax.set_ylabel('$u_a, i_c$')
ax = fig.add_subplot(212)
ax.plot(time, 10*i_e, 'red')
ax.plot(time, voltage_max*np.sin(2*np.pi*frequency*time), 'darkgreen')
ax.set_ylabel('$u_e, 10 cdot i_e$')
ax.set_xlabel('t')
ax.grid()
plt.show()
