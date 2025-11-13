def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero not allowed"
    
while True:
    print("\n Menu:")
    print("1. Suma")    
    print("2. Resta")    
    print("3. Multiplicacion")    
    print("4. Division")    
    print("5. Salir")
    
    choice = input("Enter your choice: ")    
    
    if choice=="5":
        print("Saliendo del programa")
        break
    num1= float(input("Primer numero: "))
    num2= float(input("Segundo numero: "))
    if choice=="1":
        print("Resultado: ", add(num1,num2))
    elif choice=="2":
        print("Resultado: ", substract(num1,num2))
    elif choice=="3":
        print("Resultado: ", multiply(num1,num2))
    elif choice=="4":
        print("Resultado: ", divide(num1,num2))
    else:
        print("Eleccion no valida")    
