from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()

# cmds = [
# 'loadFile(getInstallationDirectoryPath() + "/share/doc/omc/testmodels/BouncingBall.mo")',
# "simulate(BouncingBall)",
# "plot(h)"
# ]
# for cmd in cmds:
#     answer = omc.sendExpression(cmd)
#     print("\n{}:\n{}".format(cmd, answer))

# from OMPython import OMCSessionZMQ
# # omc = OMCSessionZMQ()
# # model_path=omc.sendExpression("getInstallationDirectoryPath()") + "/share/doc/omc/testmodels/"

# from OMPython import ModelicaSystem
# ModelicaSystem(useCorba=True)
# mod=ModelicaSystem(model_path + "BouncingBall.mo","BouncingBall",["Modelica"])

