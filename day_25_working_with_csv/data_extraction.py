""" Squirrel census """

import pandas as pd


# get the Primary Fur Color column
census_data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary_fur_color = census_data["Primary Fur Color"].tolist()

unique_fur_colors = set(primary_fur_color)
fur_colors = list(unique_fur_colors)

color_counts = [primary_fur_color.count(color) for color in fur_colors]

# squirrel count dataframe
squirrel_count_df = pd.DataFrame(
    {
        "Fur Color": fur_colors,
        "Count": color_counts,
    }
)
squirrel_count_df.to_csv("squirrel_count.csv")
