from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_characters = password_letters + password_numbers + password_symbols
    shuffle(password_characters)

    # "".join() turns the list into a string separated by nothing
    password = "".join(password_characters)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    messagebox.showinfo(title="Copied", message="Your generated password has been copied to your clipboard.")


def save_account_info():
    website = website_entry.get()
    email_or_username = email_or_username_entry.get()
    password = password_entry.get()

    if website == "" or email_or_username == "" or password == "":
        messagebox.showinfo(title="Info Incomplete", message="Please make sure any fields aren't empty.")
    else:
        is_ok = messagebox.askokcancel(title="Account Info", message=f"These are the details you've provided:\n\n"
                                                                     f"Website: {website}\n"
                                                                     f"Email/Username: {email_or_username}\n"
                                                                     f"Password: {password}\n\n"
                                                                     f"Press ok to save.")

        if is_ok:
            with open("accounts.txt", mode="a") as file:
                file.write(f"\nWebsite: {website} | Email/Username: {email_or_username} | Password: {password}")

            website_entry.delete(0, END)
            email_or_username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_or_username_text = Label(text="Email/Username: ")
email_or_username_text.grid(column=0, row=2)

email_or_username_entry = Entry(width=35)
email_or_username_entry.grid(column=1, row=2)

password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=3, row=3)

save_button = Button(width=30, text="Save", command=save_account_info)
save_button.grid(column=1, row=4)

window.mainloop()
