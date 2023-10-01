from matplotlib import pyplot as plt
from scipy import io as sio
from scipy import interpolate as sint
import pandas as pd
# import numpy as np


filename = "mkl.mat"
file = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)
x_value = file["x_werte"]
y_value = file["y_werte"]
data = [x_value, y_value]

data_df = pd.DataFrame(data=data).transpose()
# plt.plot(data_df[0], data_df[1], "o")

spline = sint.CubicSpline(data_df[0], data_df[1])
plt.plot(data_df[0], spline(data_df[0]))

plt.show()