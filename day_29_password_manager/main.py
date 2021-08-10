""" Password Manager """

import json
import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle

import pyperclip

# ---------------------------- SEARCH PASSWORD------------------------------- #
def search_password():
    website = website_entry.get()

    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if website in data:
            email  = data[website]["email"]
            passwd = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n \
                Password: {passwd}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} \
                exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website  = website_entry.get()
    email    = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email": email,
            "password": password,
        }
    }

    if (len(website) == 0) or (len(password) == 0):
        messagebox.showinfo(
            title="Oops!", 
            message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Canvas
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website Label
website_label = tkinter.Label(text="Website:", bg="white", padx=10, pady=10)
website_label.grid(row=1, column=0)

# Website entry
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

# search button
search_button = tkinter.Button(text="Search", width=16, command=search_password)
search_button.grid(row=1, column=2)

# Email/Username Label
email_label = tkinter.Label(
    text="Email/Username:", bg="white", padx=10, pady=10
)
email_label.grid(row=2, column=0)

# Email/Username entry
email_entry = tkinter.Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "brucewayne@batman.com")

# Password label
password_label = tkinter.Label(text="Password:", bg="white", padx=10, pady=10)
password_label.grid(row=3, column=0)

# password entry
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# password button
password_button = tkinter.Button(
    text="Generate Password", command=generate_password
)
password_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
