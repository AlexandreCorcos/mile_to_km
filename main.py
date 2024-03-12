import tkinter as tk

window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=300)
window.config(pady=20, padx=20)


def miles_to_km():
    miles = float(miles_entry.get())
    kilometers = miles * 1.60934
    result_label.config(text=f"{miles} miles = {kilometers:.2f} kilometers",
                        fg="red", font=("Arial", 14, "bold"))


def km_to_miles():
    kilometers = float(km_entry.get())
    miles = kilometers / 1.60934
    result_label.config(text=f"{kilometers} kilometers = {miles:.2f} miles",
                        fg="red", font=("Arial", 14, "bold"))


# Create widgets
miles_label = tk.Label(window, text="Miles:")
miles_label.grid(row=0, column=0)

miles_entry = tk.Entry(window)
miles_entry.grid(row=0, column=1)

km_label = tk.Label(window, text="Kilometers:")
km_label.grid(row=1, column=0)

km_entry = tk.Entry(window)
km_entry.grid(row=1, column=1)

convert_button1 = tk.Button(window, text="Convert to Kilometers", command=miles_to_km)
convert_button1.grid(row=2, column=0, columnspan=2)

convert_button2 = tk.Button(window, text="Convert to Miles", command=km_to_miles)
convert_button2.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(window, text="", fg="red", font=("Arial", 14, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

window.mainloop()
