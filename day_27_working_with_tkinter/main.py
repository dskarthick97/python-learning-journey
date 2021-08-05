import tkinter


def button_click():
    label.config(text=entry.get())


window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# Label
label = tkinter.Label(text="New Text")
label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click me", command=button_click)
button.grid(column=1, row=1)

another_button = tkinter.Button(text="Click me too!")
another_button.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)


window.mainloop()
