""" Password Manager """

import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle

import pyperclip

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

    if (len(website) == 0) or (len(password) == 0):
        messagebox.showinfo(
            title="Oops!", 
            message="Please make sure you haven't left any fields empty."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"Details entered: \nEmail: {email} \nPassword: {password} \
                \nIs is ok to save?"
        )
        
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

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
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email/Username Label
email_label = tkinter.Label(
    text="Email/Username:", bg="white", padx=10, pady=10
)
email_label.grid(row=2, column=0)

# Email/Username entry
email_entry = tkinter.Entry(width=35)
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
password_button.grid(column=2, row=3)

# add button
add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
