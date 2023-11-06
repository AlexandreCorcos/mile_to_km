from tkinter import *

FONT = ("Arial", 20, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(pady=20, padx=20)


def calculate():
    miles = float(e_converter.get())
    km = round(miles * 1.609)
    l_result.config(text=f"{km}")
    return km


# Labels
l_miles = Label(text="Miles", font=FONT)
l_miles.grid(column=2, row=0)

l_isequalto = Label(text="is equal to", font=FONT)
l_isequalto.grid(column=0, row=1)

l_km = Label(text="Km", font=FONT)
l_km.grid(column=2, row=1)

l_result = Label(text="0", font=FONT)
l_result.grid(column=1, row=1)
l_result.config(padx=10, pady=10)

# Button
b_calculate = Button(text="Calculate", command=calculate, font=FONT)
b_calculate.grid(column=1, row=2)

# Entry
e_converter = Entry(width=10, font=FONT)
e_converter.grid(column=1, row=0)

window.mainloop()
