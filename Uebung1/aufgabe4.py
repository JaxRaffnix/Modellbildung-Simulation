import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
import pandas as pd
import scipy.interpolate as sci

# Load data from the mat file as dataframe
filename = "mkl.mat"
file = loadmat(filename, squeeze_me=True)
data_df = pd.DataFrame({'x': file["x_werte"], 'y': file["y_werte"]})

# Create a spline interpolation
s = 5
spline = sci.splrep(data_df['x'], data_df['y'], s=s)
spline_x = np.arange(0, 1.5, 0.01)
spline_eval = sci.splev(spline_x, spline)
# spline_3d = sci.CubicSpline(data_df['x'], data_df['y'])

# Plot the original data and the spline interpolation
plt.plot(data_df['x'], data_df['y'], 'o', label='Original Data')
plt.plot(spline_x, spline_eval, label='One-Dimensional Spline Interpolation')
# plt.plot(data_df['x'], spline_3d(data_df['x'], 0), label='Cubic Spline Interpolation')

# Show the plot
plt.legend()
plt.show()
