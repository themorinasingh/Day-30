from tkinter import *
from tkinter import messagebox
from passGen import password_generator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password = password_generator()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_name.get().lower()
    username = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email" : username,
            "password": password
        }
    }

    if len(website) < 1 or len(password) < 1 or len(username) <1:
        messagebox.showinfo(title="OOPS!" ,message="Please don't leave any fields Empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                #json.dump(new_data, data_file)
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)


        finally:
            website_name.delete(0, END)
            password_input.delete(0, END)


#the reading and the writing of the json file can not be done, either you read or you write
#thats why angela, use 2 write statements
#got an error when file was empty
#got an error when file not found
# ---------------------------- Creating search functionality ------------------------------- #
def search_item():
    website = website_name.get().lower()
    try:

        with open("data.json") as data_file:
            data = json.load(data_file)
            username = data[website]["email"]
            password = data[website]["password"]


    except KeyError:
        website_name.delete(0, END)
        messagebox.showinfo(title=website, message=f"There is no information present about: {website}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"The data file does not Exist")

    else:
        website_name.delete(0, END)
        messagebox.showinfo(title=website, message=f"Username/Email: {username} \nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#creating the canvas and importing image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="./logo.png")
logo = canvas.create_image(100,90, image=image)
canvas.grid(column=1, row=0)

#creating Labels and entry
#todo website label
website_label = Label(text="Website: ")
website_label.grid(column= 0, row= 1)

website_name = Entry()
website_name.config(width=21)
website_name.grid(column=1,row=1)
website_name.focus()

#todo email/username label and entry
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=35)
email_input.insert(END,"theogmoe@thecyberdude.com" )
email_input.grid(column=1,row=2, columnspan=2)

#todo creating the password label and entry
password_label = Label()
password_label.config(text="Password: ")
password_label.grid(column= 0,row=3 )

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=E)

#todo create buttons

# Generate Password Button
generate_password_button = Button(text="Generate Password", width=10, command=password_gen )
generate_password_button.grid(column=2, row=3, sticky=W)

# Add Button


add_button = Button()
add_button.config(text="Add", width=34, borderwidth=0, command=save_data)
add_button.grid(column=1, row=4 , columnspan=2)

#search button
search_button = Button()
search_button.config(text="Search", width=10, command=search_item)
search_button.grid(column=2,row=1 )




window.mainloop()