import os
from math import sqrt

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.GREEN + """-------------------------------------------------------------------------
                        FUNKCIJU KALKULATORS                             
-------------------------------------------------------------------------""" + color.END)
print(color.BOLD + """Izvēlies funkcijas veidu
""" + color.END)
print("1. Lineāra funkcija (y=kx+m) \n2. Kvadrāt funkcija (y=ax^2+bx+c)") 
izvele = input(color.GREEN + "\nIevadi attiecīgo skaitli:" + color.END)


if izvele == 2 or "2.":
    cls() 
    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""*y=ax^2+bx+c
   ^
Šī vērtība
        """)
    a = float(input(color.BOLD + "\nIevadi funkcijas a vertību:" + color.END))
    cls()
    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""*y=ax^2+bx+c
        ^
    Šī vērtība
        """)
    b = float(input(color.BOLD + "Ievadi funkcijas b vertību:" + color.END))
    cls()
    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""*y=ax^2+bx+c
           ^
       Šī vērtība
        """)
    c = float(input(color.BOLD + "Ievadi funkcijas c vertību:" + color.END))
    cls()

    x0 = -b / (2*a)
    y0 = a*(x0**2) + b*x0 + c

    r = b**2 - 4*a*c


while True:

    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print(color.BOLD + "Izvēlies ko vēlies apreiķināt" + color.END)
    print("\n1. Funkcijas virziens\n2. Krustpunktu ar y un x asi\n3. Funkcijas virsotne\n4. Definīcijas un vērtību apgabals\n")
    k_izvele = input(color.GREEN + "Ievadi attiecīgo skaitli:" + color.END)
    
    if k_izvele == "1." or k_izvele == "1":
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        if a > 0:
            print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
            print(color.GREEN + "AUGŠU\n" + color.END)
            op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        if a < 0:
            print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
            print(color.GREEN + "LEJU\n" + color.END)
            op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        if op == "x":
            cls()
            continue
        if op == "exit":
            cls()
            exit()
        
    elif k_izvele == "2." or k_izvele == "2":
        
        cls()
        print(color.GREEN + "------------Krustpunkts ar x un y asi------------\n" + color.END)
        if r > 0:
            num_roots = 2
            x1 = (((-b) + sqrt(r))/(2*a))     
            x2 = (((-b) - sqrt(r))/(2*a))
            print(color.BOLD +"2 x ass krustpunkti:" + color.END)
            print(color.GREEN + f"x1 = {x1} un x2 = {x2}\n"+ color.END)
            print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
            print(color.GREEN + f"y = {c}\n" + color.END)

            op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        elif r == 0:
            num_roots = 1
            x = (-b) / 2*a
            print(color.BOLD + "1 x ass krustpunkts: " + color.END)
            print(color.GREEN + f"x = {x}\n" + color.END)
            print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
            print(color.GREEN + f"y = {c}\n" + color.END)
            
            op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        else:
            num_roots = 0
            print(color.GREEN + "Nav x ass krustpunktu, diskriminants ir mazāks par 0\n" + color.END)
            print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
            print(color.GREEN + f"y = {c}\n" + color.END)
            
            op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        if op == "x":
            cls()
            continue
        if op == "exit":
            cls()
            exit()

    elif k_izvele == "3." or k_izvele == "3":
        cls()
        print(color.GREEN + "------------Funkcijas virsotne------------\n" + color.END)
        print(color.BOLD + "Kvadrāt funkcijas virsotnes kordinātes ir:" + color.END)
        print(color.GREEN + f"({x0};{y0})\n" + color.END)
        op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        if op == "x":
            cls()
            continue
        if op == "exit":
            cls()
            exit()

    elif k_izvele == "4." or k_izvele == "4":
        cls()
        print(color.GREEN + "------------Definīcijas un vērtību apgabals------------\n" + color.END)
        if a > 0:
            print(color.GREEN + f"""D(f) = (-∞;+∞)\nE(f) = [{y0};+∞)\n""" + color.END)
        op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
        
        if a < 0:
            print(color.GREEN + f"""D(f) = (-∞;+∞)\nE(f) = (-∞;{y0})\n""" + color.END)
        op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()        
        
        if op == "x":
            cls()
            continue
        if op == "exit":
            cls()
            exit()