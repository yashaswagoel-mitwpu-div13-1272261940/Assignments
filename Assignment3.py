a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
def pythagoras(a,b,c):
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Given triangle is right angled")
    else:
        print("Given triangle is not right angled")
pythagoras(a,b,c)
