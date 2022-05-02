def test():
    print("its a test")
    
def test2():
    return "its a test 2"

def sayHello(name = "Mariana"):
    print(f"Hello {name}")

#Ingresar varios argumentos para formar una tupla
def sayHelloToEveryone(*names):
    for name in names:
        print(f"Hello {name}")

def getData(**data):
    print(f"Nombre: {data['name']}")
    print(f"Nombre: {data['last_name']}")

test()
print(test2())
sayHello("nombre")
sayHello()
sayHelloToEveryone("Orlando", "Felipe", "Cristian")
getData(name = "Mariana", last_name = "Giraldo")