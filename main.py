from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    result = miles * 1.60934
    km_result_label.config(text=f"{result:.3f} Km")

window = Tk()
window.title("Miles to KiloMeter Converter")
window.minsize(300, 200)
window.config(padx=50, pady=50)

miles_label = Label(text="Miles:", font=("Times New Roman", 13, "bold"))
miles_label.grid(column=3, row=2)

miles_input = Entry()
miles_input.grid(column=4, row=2)

space_label1 = Label(text=" ")
space_label1.grid(column=4, row=4)

cal_button = Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=4, row=6)

space_label2 = Label(text=" ")
space_label2.grid(column=4, row=8)

result_label = Label(text=f"Result:",font=("Times New Roman", 16, "bold"))
result_label.grid(column=3, row=10)

km_result_label = Label(text="0 Km",font=("Times New Roman", 16, "bold"))
km_result_label.grid(column=4, row=10)

window.mainloop()