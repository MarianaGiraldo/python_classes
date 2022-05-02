# Getting name
name = input("Please, enter your name:  ")

# Getting phone
phone = input("Please, enter your phone:  ")

# Getting email
email = input("Please, enter your email:  ")

# Getting document
document = input("Please, enter your document number:  ")

# Getting address
address = input("Please, enter your address:  ")

dicc = {
    "name" : name,
    "phone": phone,
    "email": email,
    "document": document,
    "address": address
}

print(f"\n El nombre del usuario es:\n {dicc.get('name', 'El usuario no tiene nombre')}")
print(dicc.values())