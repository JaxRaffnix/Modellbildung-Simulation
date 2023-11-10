from OMPython import ModelicaSystem
import matplotlib.pyplot as plt

modelname = "resonant_circuit"
model = ModelicaSystem(modelname+".mo", modelname)
# model.setSimulationOptions('stopTime=5.0')

model.simulate()
output_voltage = model.getSolutions("u_a")
input_voltage = model.getSolutions("u_e")
time = model.getSolutions('time')
# print(output_voltage)

fig, ax1 = plt.subplots()
ax1.plot(time[0], output_voltage[0], label="U_a")
ax1.set_xlabel("time in s")
ax1.set_ylabel("Output Voltage in V")

ax2 = ax1.twinx()
ax2.plot(time[0], input_voltage[0], label="U_e", color ="red")
ax2.set_ylabel("Input Voltage in V")

plt.title("Output voltage of the resonant circuit")
fig.legend()
plt.show()

#!! Lösung: rooyen