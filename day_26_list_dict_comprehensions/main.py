""" NATO Alphabet game """

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df_dict = {row.letter: row.code for _, row in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word: ")
phontic_names = [df_dict.get(letter) for letter in name.upper()]
print(phontic_names)
