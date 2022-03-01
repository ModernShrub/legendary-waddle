import hashlib as h
from tkinter import *
from tkinter import messagebox
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")
fbase = firebase.FirebaseApplication("https://project-mk1-default-rtdb.firebaseio.com/", None)

login_username_entry = ""
login_password_entry = ""

def login(): 
    global login_username_entry
    global login_password_entry
    
    username = login_username_entry.get()
    username = username.lower()
    password = login_password_entry.get()
    encpswrd = h.md5(password.encode())
    hex_string = encpswrd.hexdigest()
    print(username)
    print(password)
    print(encpswrd)
    print(hex_string)
    gpswrd = fbase.get("/", username)
    print(gpswrd)
    if(gpswrd != None):
        if(gpswrd == hex_string):
            messagebox.showinfo("Success", "Successfully logged in")
        else:
            messagebox.showerror("Error", "Something's wrong, I can feel it.")
    else:
        messagebox.showerror("Error", "Please check your username and/or password")
    
def register(): 
    username = username_entry.get()
    username = username.lower()
    password = password_entry.get()
    encpswrd = h.md5(password.encode())
    hex_string = encpswrd.hexdigest()
    print(username)
    print(password)
    print(encpswrd)
    print(hex_string)
    fbase.put("/", username, hex_string)
    
def login_window():
    global login_username_entry
    global login_password_entry
    
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold')
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13')
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13')
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT)
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold')
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13')
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13')
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT)

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()