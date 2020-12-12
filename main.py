from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.insert(0, password_generator())


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = ""

    return password.join(password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    global error_label
    website = website_input.get().strip()
    user_email = user_email_input.get().strip()
    password = password_input.get().strip()
    error_label.config(text="")
    if website and user_email and password:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Entry Details:\n\nEmail:  {user_email}\nPassword:  {password}\n\nIs "
                                               f"it ok?")
        if is_ok:
            with open(file="stored_passwords.txt", mode="a") as file:
                file.write(f"{website}" + " | " + f"{user_email}" + " | " + f"{password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        error_label.config(text="Error:\nEmpty or Whitespace Field is not Allowed ")
        error_label.grid(row=5, column=1)


# ---------------------------- UI SETUP ------------------------------- #


# Prepare TK Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

error_label = Label(text="", fg="red")

# Creating Logo Canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Creating and placing labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=W)
E_U_label = Label(text="Email/Username:")
E_U_label.grid(row=2, column=0, sticky=W)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=W)

# Creating and placing Entries
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2, sticky=W)
website_input.focus()
user_email_input = Entry(width=40)
user_email_input.grid(row=2, column=1, columnspan=2, sticky=W)
user_email_input.insert(0, "walid.salem@example.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=W)

# Creating and placing Buttons
generate_password_button = Button(width=15, text="Generate_password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=W)
add_button = Button(text="Add", width=36, command=store_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
