# from OMPython import ModelicaSystem
# import matplotlib.pyplot as plt

# modelname='pendel'
# mod=ModelicaSystem(modelname+'.mo',modelname)
# mod.setSimulationOptions("stopTime=5.0")
# mod.simulate()
# [t]=mod.getSolutions('time')
# [phi]=mod.getSolutions('phi')

# from OMPython import OMCSessionZMQ
# omc = OMCSessionZMQ()
# cmds = [
#   'loadFile(getInstallationDirectoryPath() + "/share/doc/omc/testmodels/BouncingBall.mo")',
#   "simulate(BouncingBall)",
#   "plot(h)"
#   ]
# for cmd in cmds:
#   answer = omc.sendExpression(cmd)
#   print("\n{}:\n{}".format(cmd, answer))

from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()
model_path=omc.sendExpression("getInstallationDirectoryPath()") + "/share/doc/omc/testmodels/"
from OMPython import ModelicaSystem
mod=ModelicaSystem(model_path + "BouncingBall.mo","BouncingBall")