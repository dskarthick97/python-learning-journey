""" Letter generator """

# read the invited_names.txt files
# convert it to the list
with open("./Input/Names/invited_names.txt", mode="r") as file:
    contents = file.read()
    names = contents.split(sep="\n")
    

# read the starting_letter file
with open("./Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.read()
    for name in names:
        new_contents = contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
            output_file.write(new_contents)
