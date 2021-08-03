import os

import psutil
import pandas as pd

data = pd.read_csv("./weather_data.csv")
temperature = data["temp"]  # we can also get the columns of the dataframes as attributes. Eg. data.temp

# computations
avg_temp = temperature.mean()
print(avg_temp)
max_temp = temperature.max()
print(max_temp)

# retrieving a row in dataframe
row = data[data.day == "Monday"]
print(row)

# retrieving a row that has max temp
row_with_max_temp = data[data.temp == data.temp.max()]
print(row_with_max_temp)

print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
