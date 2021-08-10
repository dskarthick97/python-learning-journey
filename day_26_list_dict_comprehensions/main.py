""" NATO Alphabet game """

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df_dict = {row.letter: row.code for _, row in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    name = input("Enter a word: ")
    try:
        phontic_names = [df_dict.get(letter) for letter in name.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phontic_names)


generate_phonetic()
