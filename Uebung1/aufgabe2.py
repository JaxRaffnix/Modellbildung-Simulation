import numpy as np
import pandas as pd

# import csv file
filename = "magic_matrix.csv"
# matrix = np.loadtxt(filename, delimiter=",")
array = pd.read_csv(filename)

# a csv file stores information as a a table. rows are seperated by a new line, columns are seperated by commas.

print(array)