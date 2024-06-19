import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import showinfo

# App Settings
app = tk.Tk()
app.configure(bg="white")
app.geometry("300x400")
app.title("Simple CRUD")

# Dictionary
data = {
    "Nama Barang": ["Roti", "Air Mineral", "Pentol"],
    "Harga Barang": [2000, 4000, 2000],
    "Kuantitas":[12, 22, 12]
}

# Frame
loginFrame = ttk.Frame(app)
loginFrame.pack(fill = "both", expand = True)

# Menu Login

# Variabel
usernameVar = tk.StringVar()
passwordVar = tk.StringVar()

# Username
# Label
usernameLabel = ttk.Label(loginFrame, text = "Username")
usernameLabel.pack()

# Input
usernameEntry = ttk.Entry(loginFrame, textvariable = usernameVar)
usernameEntry.pack()

# Password
# Label
passwordLabel = ttk.Label(loginFrame, text = "Password")
passwordLabel.pack()

# Input
passwordEntry = ttk.Entry(loginFrame, textvariable = passwordVar)
passwordEntry.pack()

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

# Create Menu
def createWindow():
    # Window Settings
    createWindow = tk.Toplevel(app)
    createWindow.title("Create Menu")
    createWindow.geometry("300x400")

    # Variabel
    nameVar = tk.StringVar()
    priceVar = tk.IntVar()
    quantityVar = tk.IntVar()

    # Item Name
    # Label
    nameLabel = tk.Label(createWindow, text = "Masukkan Nama Barang")
    nameLabel.pack(pady = 5)

    # Input
    nameEntry = tk.Entry(createWindow, textvariable = nameVar)
    nameEntry.pack(pady = 5)

    # Item Price
    # Label
    priceLabel = tk.Label(createWindow, text = "Masukkan Harga Barang")
    priceLabel.pack(pady = 5)

    # Input
    priceEntry = tk.Entry(createWindow, textvariable = priceVar)
    priceEntry.pack(pady = 5)

    # Quantity
    # Label
    qtyLabel = tk.Label(createWindow, text = "Masukkan Kuantitas")
    qtyLabel.pack(pady = 5)

    # Input
    qtyEntry = tk.Entry(createWindow, textvariable = quantityVar)
    qtyEntry.pack(pady = 5)

    def enterData():
        name = nameVar.get()
        price = priceVar.get()
        quantity = quantityVar.get()
        create(name, price, quantity)
    enterButton = ttk.Button(createWindow, text = "Enter", command = enterData)
    enterButton.pack(pady = 5)

# Untuk Memasukkan Data
def create(name, price, quantity):
    if name.strip():
        if str(price).strip():
            if str(quantity).strip():
                data["Nama Barang"].append(name)
                data["Harga Barang"].append(price)
                data["Kuantitas"].append(quantity)
                print(data)
                showinfo(title = "Pesan", message = f"Barang {name} Berhasil Ditambahkan Ke Database")
            else:
                showinfo(title = "Pesan", message = "Kuantitas Tidak Boleh Kosong")
        else:
            showinfo(title = "Pesan", message = "Harga Tidak Boleh Kosong")
    else:
        showinfo(title = "Pesan", message = "Nama Tidak Boleh Kosong")

# Read Menu
def readWindow():
    # Window Settings
    readWindow = tk.Toplevel(app)
    readWindow.title("Read Menu")
    readWindow.geometry("300x400")

    # Table
    table = ttk.Treeview(readWindow, columns = ("Nama", "Harga", "Kuantitas"), show = "headings")

    table.heading("Nama", text = "Nama Barang")
    table.heading("Harga", text = "Harga Barang")
    table.heading("Kuantitas", text = "Kuantitas")
    table.pack(fill = "both", expand = True)

    for i in range(len(data["Nama Barang"])):
        table.insert(parent = "", index = 0, values = (data["Nama Barang"][i], data["Harga Barang"][i], data["Kuantitas"][i]))

createButton = ttk.Button(crudMenuFrame, text = "Create", command = createWindow)
createButton.pack(pady = 5)
readButton = ttk.Button(crudMenuFrame, text = "Read", command = readWindow)
readButton.pack(pady = 5)
updateButton = ttk.Button(crudMenuFrame, text = "Update")
updateButton.pack(pady = 5)
deleteButton = ttk.Button(crudMenuFrame, text = "Delete")
deleteButton.pack(pady = 5)

# Loop
app.mainloop()
