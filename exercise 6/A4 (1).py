from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files


modelname='A4'
mod=ModelicaSystem(modelname+'.mo',modelname,['./ModSimBib/package.mo'])
mod.setSimulationOptions('stopTime=0.040')
mod.simulate()
[t]=mod.getSolutions('time')
[i_L]=mod.getSolutions('inductor1.i')
[u]=mod.getSolutions('vierqst1.u_out')
delete_OM_files(modelname)

fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, 5*i_L, 'r')
ax.plot(t, u, 'darkgreen')
ax.grid()
ax.set_xlabel('t/s')
ax.set_ylabel('u/v bzw. 5*i/A')

fig.tight_layout()
