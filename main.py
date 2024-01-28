from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "me@gmail.com")
password_entry = Entry(width=19)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=17, command=password_generator)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# ---------------------------- OLD SAVE PASSWORD ------------------------------- #
# def save_password():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#
#     if len(website) == 0 or len(password) == 0:
#         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
#                                                               f"Email: {email}\nPassword: {password}\n"
#                                                               f"Is it ok to save?")
#
#         if is_ok:
#             # data_file = open("data.txt", "a")
#             # data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
#             # data_file.close()
#
#             # Щоб не писати close()
#             with open("data.txt", "a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
