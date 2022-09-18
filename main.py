from tkinter import *
from tkinter import messagebox
import random
import json
from turtle import width
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def password_generation():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    
    password_entry.insert(0,password)


def save():
    website=web_entry.get()
    emails=email_entry.get()
    passw=password_entry.get()
    data_dic={
        website:{
        "email":emails,
        "password":passw,}
    }
    if len(website)==0 or len(emails)==0 or len(passw)==0:
        
        messagebox.showinfo(title="Oops" ,message="Please enter every details")
    else:
        is_ok=messagebox.askyesno(title=website,message=f"There are the details entered \n website :- {website}\nEmail/Username :- {emails}\npassward :- {passw}")
        if is_ok:
            try:
                with open("data.json","r") as file_data:
                    data=json.load(file_data)
                    data.update(data_dic)
            except:
                with open("data.json","w") as file_data:
                    json.dump(data_dic,file_data,indent=4)
            else:

                with open("data.json","w") as file_data:
                    json.dump(data,file_data,indent=4)
                    web_entry.delete(0,END)
                    email_entry.delete(0,END)
                    password_entry.delete(0,END)



def gotdata():
    website=web_entry.get()
    try:
        with open("data.json","r") as data_file:
            dic=json.load(data_file)
    except :
        messagebox.showerror(message="data not founded")
    else:
        if website in dic:
            email=dic[website]["email"]
            passw=dic[website]["password"]
            messagebox.showinfo(title=website,message=f"email : {email}\npassword : {passw}")
        else:
            messagebox.showinfo(message="data not found")
            web_entry.delete(0,END)

tk_object=Tk()

tk_object.title("Passward Manager")
image_logo=PhotoImage(file="logo.png")
tk_object.config(padx=70,pady=70)
canvas=Canvas(width=200,height=200)

logo=canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)


web=Label(text="Website")
web.grid(row=1,column=0)
web.focus()

email=Label(text="Email/Username")
email.grid(row=2,column=0)

password=Label(text="Password")
password.grid(row=3,column=0)

web_entry=Entry(width=32)
web_entry.grid(row=1,column=1)

email_entry=Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=32)
password_entry.grid(row=3,column=1)

password_botton=Button(text="Generate Password",command=password_generation)
password_botton.grid(row=3,column=2)

add_button=Button(text="Add",width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search=Button(text="Search",width=15,command=gotdata)
search.grid(row=1,column=2)
tk_object.mainloop()
