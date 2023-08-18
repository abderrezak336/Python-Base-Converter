from tkinter import *
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


def reset():
    user_entry.delete(0, END)
    result_entry.delete(0, END)





def binary_to_decimal():
    """this function convert binary number into decimal number"""
    number = user_entry.get()
    power = type_of_number.get()
    total = 0
    length = len(str(number)) - 1
    for i in number:
        total += int(i) * (int(power)**length)
        length -= 1
    result_entry.insert(END, string=f"{total}")

def decimal_to_binary():
    """this function convert decimal numner to binary"""
    number = int(user_entry.get())
    list_of_reminders = []
    divisor = int(second_type_of_number.get())
    while number // divisor != 0:
        reminder = number % divisor
        list_of_reminders.append(reminder)
        number //= divisor
        if number // divisor == 0:
            list_of_reminders.append(number)
    list_of_reminders.reverse()
    number_in_binary = ""
    for i in list_of_reminders:
        number_in_binary += str(i)
    result_entry.insert(END, string=f"{number_in_binary}")







window = Tk()
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)





title = "system of number converter"
window.title(title.title())




photo = PhotoImage(file=r"calculator.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=0, columnspan=4)

def show_details():
    message = """
    Note --> this application can only convert
    binary to decimal
    octal to decimal
    hexdecimal to decimal
    decimal to binary
    decimal to octal
    decimal to hexdecimal"""
    messagebox.showinfo(title="Details", message=message)




#from text label
from_label = Label(text="From Base", font=("arial", 15, "normal"), fg=RED)
from_label.grid(row=1, column=0)


#entry
user_entry = Entry(width=15)
user_entry.grid(row=2, column=1)


#to text label
to_label = Label(text="To Base", font=("arial", 15, "normal"), fg=RED)
to_label.grid(row=1, column=2)


label = Label(text="type your number here -->")
label.grid(row=2, column=0)



#result entry
result_entry = Entry(width=15)
result_entry.grid(row=2, column=3)


def choice():
    type_1 = type_of_number.get()
    type_2 = second_type_of_number.get()
    if type_1 == "2" and type_2 == "10" or type_1 == "8" and type_2 == "10" or type_1 == "16" and type_2 == "10":
        binary_to_decimal()
    elif type_1 == "10" and type_2 == "2" or type_1 == "10" and type_2 == "16" or type_1 == "10" and type_2 == "8":
        decimal_to_binary()




type_of_number = Entry(width=15)
type_of_number.insert(END, string="2")
type_of_number.grid(row=1, column=1)





second_type_of_number = Entry(width=15)
second_type_of_number.insert(END, "10")
second_type_of_number.grid(row=1, column=3)





#calculat button
calculate = Button(text="Calculate", width=10, command=choice, bg=GREEN)
calculate.grid(row=3, column=2)


#remove button
remove = Button(text="Remove", width=10, bg=PINK, command=reset)
remove.grid(row=4, column=2)

#details button
detatils = Button(text="Detail", width=10, command=show_details)
detatils.grid(row=5, column=2)


window.mainloop()