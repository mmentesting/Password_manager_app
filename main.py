from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("arial", 9, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(5, 7))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_account():
    user_search = web_entry.get()
    try:
        with open("data.txt") as data_file:
            data = data_file.readlines()
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        email = ""
        for row in data:
            row_items = row.split(" | ")
            if user_search.title() == row_items[0].title():
                email = row_items[1]
                password = row_items[2]
        if email != "":
            messagebox.showinfo(title=f"{user_search}", message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"{user_search} Not found!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = web_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    if len(web_text) == 0 or len(password_text) == 0 or len(email_text) == 0:
        messagebox.showinfo(title="Warning", message="Oops! Please don't leave empty fields!")
    else:
        is_ok = messagebox.askokcancel(
            title=web_text,
            message=f"Details entered: \nEmail:{email_text}\nPassword: {password_text} \npress OK to save.")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web_text} | {email_text} | {password_text}\n")
            messagebox.showinfo(title="Success", message=f"{web_text} added to the data file.")
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:", font=FONT)
web_label.grid(column=0, row=1, sticky="w")
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3, sticky="w")

web_entry = Entry(width=30)
web_entry.focus()
web_entry.grid(column=1, row=1)
email_entry = Entry(width=50)
email_entry.insert(0, string="useremail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", font=FONT, width=15, command=search_account)
search_button.grid(column=2, row=1, sticky="e")
generate_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_button.grid(column=2, row=3, sticky="e")
add_button = Button(text="Add", font=FONT, width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
