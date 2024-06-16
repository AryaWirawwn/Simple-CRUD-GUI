import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import showinfo

# App Settings
app = tk.Tk()
app.configure(bg="white")
app.geometry("512x256")
app.title("Simple CRUD")

# Frame
loginFrame = ttk.Frame(app)
loginFrame.pack(padx = 10, pady = 10, fill = "x", expand = True)

# Menu Login

# Variabel
usernameVar = tk.StringVar()
passwordVar = tk.StringVar()

# Username
# Label
usernameLabel = ttk.Label(loginFrame, text = "Username")
usernameLabel.pack(fill = "x", expand = True)

# Input
usernameEntry = ttk.Entry(loginFrame, textvariable = usernameVar)
usernameEntry.pack(fill = "x", expand = True)

# Password
# Label
passwordLabel = ttk.Label(loginFrame, text = "Password")
passwordLabel.pack(fill = "x", expand = True)

# Input
passwordEntry = ttk.Entry(loginFrame, textvariable = passwordVar)
passwordEntry.pack(fill = "x", expand = True)

# Login
def login():
    username = usernameVar.get()
    password = passwordVar.get()
    if username == "admin" and password == "admin":
        pesan = "Selamat Datang Admin"
        showinfo(title = "Pesan", message = pesan)
        loginFrame.pack_forget()
        crudMenu()
    elif username != "admin" and password == "admin":
        pesan = "Username Salah!"
        showinfo(title = "Pesan", message = pesan)
    elif username == "admin" and password != "admin":
        pesan = "Password Salah!"
        showinfo(title = "Pesan", message = pesan)
    else:
        pesan = "Username dan Password Salah!"
        showinfo(title = "pesan", message = pesan)

loginButton = ttk.Button(loginFrame, text = "Login", command = login)
loginButton.pack(pady = 10)

# Menu CRUD
crudMenuFrame = ttk.Frame(app)

def crudMenu():
    crudMenuFrame.pack(fill = "both", expand = True)

createButton = ttk.Button(crudMenuFrame, text = "Create")
createButton.pack(pady = 5)
readButton = ttk.Button(crudMenuFrame, text = "Read")
readButton.pack(pady = 5)
updateButton = ttk.Button(crudMenuFrame, text = "Update")
updateButton.pack(pady = 5)
deleteButton = ttk.Button(crudMenuFrame, text = "Delete")
deleteButton.pack(pady = 5)
# Loop
app.mainloop()
