from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # data_file = open("data.txt", "a")
    # data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
    # data_file.close()

    # Щоб не писати close()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
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
email_entry.insert(0, "angela@gmail.com")
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
