from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

with np.load("messwerte.npz", ) as file:
    t = file["t_mess"]
    u_a = file["u_a_mess"]
    
    data = pd.DataFrame({"t": t, "u_a": u_a})
    

plt.plot(data["t"], data["u_a"], label="Messwerte")
plt.show()