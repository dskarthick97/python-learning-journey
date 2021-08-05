""" Miles to Km Converter """

import tkinter


def convert():
    mile = mile_entry.get()
    km = float(mile) * 1.609344
    km_result_label.config(text=round(km, 2))


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=40, pady=20)

# Entry
mile_entry = tkinter.Entry(width=15)
mile_entry.grid(column=1, row=0, padx=10, pady=10)

# Miles Label
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0, padx=10, pady=10)

# Is equal to Label
is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1, padx=10, pady=10)

# Label
km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1, padx=10, pady=10)

# Km Label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1, padx=10, pady=10)

# Calculate button
calculate_button = tkinter.Button(text="Calculate", width=10, command=convert)
calculate_button.grid(column=1, row=2, padx=10, pady=10)


window.mainloop()
