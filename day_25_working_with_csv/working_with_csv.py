""" Working with csv files """

# read the weather_data.csv file contents
# with open("./weather_data.csv") as weather_file:
#     data = weather_file.readlines()


# # using csv module
import csv
import os

import psutil

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = [int(row[1]) for row in data if row[1] != "temp"]
    print(temperatures)

print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

# using pandas module
# import pandas as pd

# data = pd.read_csv("./weather_data.csv")
# print(data)
