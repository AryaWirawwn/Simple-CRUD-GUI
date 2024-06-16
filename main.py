import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import showinfo

# App Settings
app = tk.Tk()
app.configure(bg="white")
app.geometry("512x256")
app.title("Simple CRUD")

# Frame
frameApp = ttk.Frame(app)
frameApp.pack(padx = 10, pady = 10, fill = "x", expand = True)

# Menu Login

# Variabel
usernameVar = tk.StringVar()
passwordVar = tk.StringVar()

# Username
# Label
usernameLabel = ttk.Label(frameApp, text = "Username")
usernameLabel.pack(fill = "x", expand = True)

# Input
usernameEntry = ttk.Entry(frameApp, textvariable = usernameVar)
usernameEntry.pack(fill = "x", expand = True)

# Password
# Label
passwordLabel = ttk.Label(frameApp, text = "Password")
passwordLabel.pack(fill = "x", expand = True)

# Input
passwordEntry = ttk.Entry(frameApp, textvariable = passwordVar)
passwordEntry.pack(fill = "x", expand = True)

# Login
def login():
    username = usernameVar.get()
    password = passwordVar.get()
    if username == "admin" and password == "admin":
        pesan = "Selamat Datang Admin"
        showinfo(title = "Pesan", message = pesan)
    elif username != "admin" and password == "admin":
        pesan = "Username Salah!"
        showinfo(title = "Pesan", message = pesan)
    elif username == "admin" and password != "admin":
        pesan = "Password Salah!"
        showinfo(title = "Pesan", message = pesan)
    else:
        pesan = "Username dan Password Salah!"
        showinfo(title = "pesan", message = pesan)

loginButton = ttk.Button(frameApp, text = "Login", command = login)
loginButton.pack(fill = "x", expand = True, pady = 10)

# Loop
app.mainloop()