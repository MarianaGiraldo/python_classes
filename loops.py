# x = int(input("Enter a number: "))
# #Conditional
# if ( x < 3 ):
#     print("Es menor a 3")
# elif ( x > 3):
#     print("Es mayor a 3")
# else:
#     print("Es igual a 3")

# x = int(input("Enter another number: "))
# #Inline if
# txt = "Es menor a 3" if ( x < 3 ) else "Es igual o mayor a 3"
# print(txt)

#While loop
from hashlib import new


d=5
while (d > 0):
    d -= 1
    print(d)
else: 
    print("Ya no es mayor a 0")


#For loop
txt = "Is a string"
for i in reversed(txt):
    print(i)
    
fruits = ["Apple", "banana", "Strawberry", "Watermelon"]
newList = [x for x in fruits if x != "Apple"]
print(newList)
newList = [x for x in fruits]
print(newList)

#Ingresar varios argumentos para formar una tupla
def sayHelloToEveryone(*names):
    for name in names:
        print(f"Hello {name}")

sayHelloToEveryone("Orlando", "Felipe", "Cristian")

#Enter a lot of arguments with their keys, as a dictionary
def getKidName(**kid):
    print(f"The kid's name is {kid['fname']} {kid['lname']}")
getKidName(fname= "Juan", lname="Perez")

sumar = lambda x,y : x + y
print(sumar(10,20))
