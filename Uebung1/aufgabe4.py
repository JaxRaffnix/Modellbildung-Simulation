from matplotlib import pyplot as plt
from scipy import io as sio
import pandas as pd
import numpy as np


filename = "mkl.mat"
file = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)
x_value = file["x_werte"]
y_value = file["y_werte"]
data = [x_value, y_value]
data_df = pd.DataFrame(data=data).transpose()

plt.plot(data_df[0],data_df[1])
plt.show()