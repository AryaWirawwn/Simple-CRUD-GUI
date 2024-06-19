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
    "Nomor": [1, 2, 3],
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
        showinfo(title = "Pesan", message = pesan)

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
    nameVar = tk.StringVar(value = "Nama Barang")
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
                nomor = len(data["Nomor"]) + 1
                data["Nomor"].append(nomor)
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
    table = ttk.Treeview(readWindow, columns = ("Nomor", "Nama", "Harga", "Kuantitas"), show = "headings")
    
    table.heading("Nomor", text = "Nomor")
    table.heading("Nama", text = "Nama Barang")
    table.heading("Harga", text = "Harga Barang")
    table.heading("Kuantitas", text = "Kuantitas")
    table.pack(fill = "x", expand = True)

    for i in range(len(data["Nomor"])):
        table.insert(parent = "", index = 0, values = (data["Nomor"][i], data["Nama Barang"][i], data["Harga Barang"][i], data["Kuantitas"][i]))

def updateWindow():
    # Window Settings
    updateWindow = tk.Toplevel(app)
    updateWindow.title("Update Menu")
    updateWindow.geometry("300x400")
    
    # Variabel
    itemNumberVar = tk.IntVar()

    # Update Input Number
    # Label
    updateLabelNumber = ttk.Label(updateWindow, text = "Masukkan Nomor Barang")
    updateLabelNumber.pack(pady = 5)

    # Input
    updateEntryNumber = ttk.Entry(updateWindow, textvariable = itemNumberVar)
    updateEntryNumber.pack(pady = 5)

    # Update Button
    def mainUpdateWindow():
        itemNumber = itemNumberVar.get()
        if itemNumber in data["Nomor"]:
            # Index
            index = data["Nomor"].index(itemNumber)

            # Variables
            nameVar = tk.StringVar(value=data['Nama Barang'][index])
            priceVar = tk.IntVar(value=data['Harga Barang'][index])
            quantityVar = tk.IntVar(value=data['Kuantitas'][index])

            # Name
            # Label
            updateLabelName = ttk.Label(updateWindow, text="Nama")
            updateLabelName.pack(pady=5)

            # Input
            updateEntryName = ttk.Entry(updateWindow, textvariable=nameVar)
            updateEntryName.pack(pady=5)

            # Price
            # Label
            updateLabelPrice = ttk.Label(updateWindow, text="Harga")
            updateLabelPrice.pack(pady=5)

            # Input
            updateEntryPrice = ttk.Entry(updateWindow, textvariable=priceVar)
            updateEntryPrice.pack(pady=5)

            # Quantity
            # Label
            updateLabelQuantity = ttk.Label(updateWindow, text="Kuantitas")
            updateLabelQuantity.pack(pady=5)

            # Input
            updateEntryQuantity = ttk.Entry(updateWindow, textvariable=quantityVar)
            updateEntryQuantity.pack(pady=5)

            # Button
            def saveUpdate():
                newName = nameVar.get()
                newPrice = priceVar.get()
                newQuantity = quantityVar.get()
                if newName.strip():
                    data["Nama Barang"][index] = newName
                    data["Harga Barang"][index] = newPrice
                    data["Kuantitas"][index] = newQuantity

                    showinfo(title = "Pesan", message = f"Barang Dengan Nomor {itemNumber} Berhasil Diubah")
                else:
                    showinfo(title = "Pesan", message = "Nama Tidak Boleh Kosong")

            saveUpdateButton = ttk.Button(updateWindow, text = "Save", command = saveUpdate)
            saveUpdateButton.pack(pady = 5)
        else:
            showinfo(title = "Pesan", message = f"Barang Dengan Nomor {itemNumber} Tidak Ditemukan")

    updateButton = ttk.Button(updateWindow, text = "Update", command = mainUpdateWindow)
    updateButton.pack(pady = 5)


def deleteWindow():
    # Window Settings
    deleteWindow = tk.Toplevel(app)
    deleteWindow.title("Delete Menu")
    deleteWindow.geometry("300x400")

    # Variable
    itemNumberVar = tk.IntVar()
    
    # Delete
    # Label
    deleteLabel = ttk.Label(deleteWindow, text = "Masukkan Nomor Barang")
    deleteLabel.pack(pady = 5)

    # Input
    deleteEntry = ttk.Entry(deleteWindow, textvariable = itemNumberVar)
    deleteEntry.pack(pady = 5 )

    # Button
    def deleteData():
        itemNumber = itemNumberVar.get()
        if itemNumber in data["Nomor"]:
            index = data["Nomor"].index(itemNumber)
            data["Nomor"].pop(index)
            data["Nama Barang"].pop(index)
            data["Harga Barang"].pop(index)
            data["Kuantitas"].pop(index)
            showinfo(title = "Pesan", message = f"Barang Nomor {itemNumber} berhasil dihapus")

    deleteButton = ttk.Button(deleteWindow, text = "Delete", command = deleteData)
    deleteButton.pack(pady = 5)

# Button
createButton = ttk.Button(crudMenuFrame, text = "Create", command = createWindow)
createButton.pack(pady = 5)
readButton = ttk.Button(crudMenuFrame, text = "Read", command = readWindow)
readButton.pack(pady = 5)
updateButton = ttk.Button(crudMenuFrame, text = "Update", command = updateWindow)
updateButton.pack(pady = 5)
deleteButton = ttk.Button(crudMenuFrame, text = "Delete", command = deleteWindow)
deleteButton.pack(pady = 5)

# Loop
app.mainloop()
