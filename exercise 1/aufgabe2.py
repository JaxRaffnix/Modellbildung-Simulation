import numpy as np
import pandas as pd


# a csv file stores information as a a table. rows are seperated by a new line, columns are seperated by commas.


# import csv file
filename = "magic_matrix.csv"
# matrix = np.loadtxt(filename, delimiter=",")
with pd.read_csv(filename, header=None) as array:


    # calculate the sum, min and max of all the values in the matrix
    sum = array.sum().sum()
    print("Sum: ",sum)

    max = array.max().max()
    index_max = array.idxmax()
    print("max value: ",max)
    # !!richtige Lösung
    index = np.where(array = array.max())

    min = array.min().min()
    print("min value:", min)

    # create row vector
    v_1 = array[3]
    print(v_1)

    # sum of all the values greater than 40
    sum_high = array[array > 40].sum().sum()
    print("sum of values > 40: ", sum_high)

    # new list of values from postion 3,4 to 7,4
    new_list = array.iloc[4].iloc[3:8]
    print(new_list)