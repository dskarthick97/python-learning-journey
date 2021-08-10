""" Exceptions Handling """

# FileNotFound error

try:
    file = open("file.txt")
except Exception as err:
    print(err)
    # print(dir(err))
    print(err.__cause__)
    print(err.args[1])
    print("File not found!")