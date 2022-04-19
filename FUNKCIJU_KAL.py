from __future__ import print_function
import os
from math import sqrt
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

answer_1 = ["1", "1."]
answer_2 = ["2", "2."]
answer_3 = ["3", "3."]
answer_4 = ["4", "4."]
answer_X = ["X", "x"]
answer_Y = ["Y", "y"]
answer_END = ["exit"]

required = ("\nIeveadi tikai skaitli 1 vai 2\n")
required_op = ("\nIeveadi tikai x, y vai exit\n")
required_fu = ("\nIeveadi tikai 1, 2, 3 vai 4\n")

a = 0.0
b = 0.0
c = 0.0
x0 = 0.0
y0 = 0.0
r = 0.0
k = 0.0
m = 0.0


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


def sakums():
    cls()
    print(color.GREEN + """-------------------------------------------------------------------------
                            FUNKCIJU KALKULATORS                             
-------------------------------------------------------------------------""" + color.END)
    print(color.BOLD + """Izvēlies funkcijas veidu
    """ + color.END)
    print("1. Lineāra funkcija (y=kx+m) \n2. Kvadrāt funkcija (y=ax^2+bx+c)") 
    izvele = input(color.GREEN + "\nIevadi attiecīgo skaitli:" + color.END)
    if izvele in answer_1:
        l_izvele()

    elif izvele in answer_2:
        k_izvele()
        
    else:
        cls()
        print(color.GREEN + required + color.END)
        time.sleep(2)
        cls()
        sakums()

def k_izvele():
    global a, b, c, x0, y0, r
    cls() 
    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""* y = ax^2 + bx + c
      ^
  Šī vērtība
            """)
    a = float(input(color.BOLD + "\nIevadi funkcijas a vertību:" + color.END))
    cls()

    if a == 0:
        cls()
        print(color.GREEN + "a vērtība nevar būt 0 - tad tā vairs nav kvadrāt funkcija, bet lineāra funkcija" + color.END)
        time.sleep(4)
        cls()
        k_izvele()
    

    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""* y = ax^2 + bx + c
             ^
         Šī vērtība
        """)
    b = float(input(color.BOLD + "Ievadi funkcijas b vertību:" + color.END))
    cls()

    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print("""* y = ax^2 + bx + c
                  ^
              Šī vērtība
        """)
    c = float(input(color.BOLD + "Ievadi funkcijas c vertību:" + color.END))
    
 

    x0 = -b / (2*a)
    y0 = a*(x0**2) + b*x0 + c

    r = b**2 - 4*a*c

    k_apreikins()

def k_apreikins():
    cls()
    print(color.GREEN + "------------Kvadrāt funkcija------------\n" + color.END)
    print(color.BOLD + "Izvēlies ko vēlies apreiķināt" + color.END)
    print("\n1. Funkcijas virziens\n2. Krustpunktu ar y un x asi\n3. Funkcijas virsotne\n4. Definīcijas un vērtību apgabals\n")
    skaitlis_k = input(color.GREEN + "Ievadi attiecīgo skaitli:" + color.END)


    if skaitlis_k in answer_1:
        kvad_1()
    elif skaitlis_k in answer_2:
        kvad_2()
    elif skaitlis_k in answer_3:
        kvad_3()
    elif skaitlis_k in answer_4:
        kvad_4()
    else:
        cls()
        print(color.GREEN + required_fu + color.END)
        time.sleep(2)
        cls()
        k_apreikins()


def kvad_1():
    cls()
    if a > 0:
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
        print(color.GREEN + "AUGŠU\n" + color.END)
        time.sleep(0.5)
        opt_k()
    elif a < 0:
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
        print(color.GREEN + "LEJU\n" + color.END)
        time.sleep(0.5)
        opt_k()

def opt_k():
    op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
    if op in answer_X:
        k_apreikins()      
    elif op in answer_Y:
        sakums()       
    elif op in answer_END:
        exit()
    else:
        cls()
        print(color.GREEN + required_op + color.END)
        time.sleep(2)
        cls()
        opt_k()

def opt_l():
    op = input("Ievadi x ja vēlies turpināt veikt citus apreiķinus ar šo pašu funkciju\nIevadi y ja vēlies sākt no sākuma\nIevadi exit ja vēlies iziet no programas:").lower()
    if op in answer_X:
        l_apreikins()      
    elif op in answer_Y:
        sakums()       
    elif op in answer_END:
        exit()
    else:
        cls()
        print(color.GREEN + required_op + color.END)
        time.sleep(2)
        cls()
        opt_l()

def kvad_2():
    cls()
    print(color.GREEN + "------------Krustpunkts ar x un y asi------------\n" + color.END)

    if r > 0:
        x1 = (((-b) + sqrt(r))/(2*a))     
        x2 = (((-b) - sqrt(r))/(2*a))
        print(color.BOLD +"2 x ass krustpunkti:" + color.END)
        print(color.GREEN + f"x1 = {x1} un x2 = {x2}\n"+ color.END)
        print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
        print(color.GREEN + f"y = {c}\n" + color.END)
        time.sleep(0.5)
        opt_k()

    elif r == 0:  
        x = (-b) / 2*a
        print(color.BOLD + "1 x ass krustpunkts: " + color.END)
        print(color.GREEN + f"x = {x}\n" + color.END)
        print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
        print(color.GREEN + f"y = {c}\n" + color.END)
        time.sleep(0.5)
        opt_k()
    
    else:    
        print(color.GREEN + "Nav x ass krustpunktu, diskriminants ir mazāks par 0\n" + color.END)
        print(color.BOLD + "Krustpunkts ar y asi:" + color.END)
        print(color.GREEN + f"y = {c}\n" + color.END)
        time.sleep(0.5)
        opt_k()

def kvad_3():
    cls()
    print(color.GREEN + "------------Funkcijas virsotne------------\n" + color.END)
    print(color.BOLD + "Kvadrāt funkcijas virsotnes kordinātes ir:" + color.END)
    print(color.GREEN + f"({x0};{y0})\n" + color.END)
    time.sleep(0.5)
    opt_k()

def kvad_4():
    cls()
    if a > 0:
        print(color.GREEN + f"""D(f) = (-∞;+∞)\nE(f) = [{y0};+∞)\n""" + color.END)
        time.sleep(0.5)
        opt_k()   
    elif a < 0:
        print(color.GREEN + f"""D(f) = (-∞;+∞)\nE(f) = (-∞;{y0})\n""" + color.END)
        time.sleep(0.5)
        opt_k()
        

def l_izvele():
    global k, m
    cls()
    print(color.GREEN + "------------Lineār funkcija------------\n" + color.END)
    print("""* y = kx + m
      ^
  Šī vērtība
                """)
    k = float(input(color.BOLD + "\nIevadi funkcijas k vertību:" + color.END))
    cls()

    print(color.GREEN + "------------Lineār funkcija------------\n" + color.END)
    print("""* y = kx + m
           ^
      Šī vērtība
                """)
    m = float(input(color.BOLD + "\nIevadi funkcijas m vertību:" + color.END))
    l_apreikins()

def l_apreikins():
    cls()
    print(color.GREEN + "------------Lineār funkcija------------\n" + color.END)
    print(color.BOLD + "Izvēlies ko vēlies apreiķināt" + color.END)
    print("\n1. Funkcijas virziens\n2. Krustpunktu ar y un x asi\n3. Definīcijas un vērtību apgabals\n4. Divu lineāru funkciju krustpunkti\n")
    skaitlis_l = input(color.GREEN + "Ievadi attiecīgo skaitli:" + color.END)

    if skaitlis_l in answer_1:
        lin_1()
    elif skaitlis_l in answer_2:
        lin_2()
    elif skaitlis_l in answer_3:
        lin_3()
    elif skaitlis_l in answer_4:
        lin_4()
    else:
        cls()
        print(color.GREEN + required_fu + color.END)
        time.sleep(2)
        cls()
        l_apreikins()

def lin_1():
    cls()
    if k > 0:
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
        print(color.GREEN + "AUGŠU\n" + color.END)
        time.sleep(0.5)
        opt_l()
    elif k < 0:
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        print(color.BOLD +"Kvadrāt funkcijas virziens ir uz:" + color.END)
        print(color.GREEN + "LEJU\n" + color.END)
        time.sleep(0.5)
        opt_l()
    elif k == 0:
        cls()
        print(color.GREEN + "------------Funkcijas virziens------------\n" + color.END)
        print(color.BOLD +"Kvadrāt funkcijas virziens ir:" + color.END)
        print(color.GREEN + "KONSTANTA jeb nemainīga\n" + color.END)
        time.sleep(0.5)
        opt_l()

def lin_2():
    cls()
    print(color.GREEN + "------------Krustpunkts ar x un y asi------------\n" + color.END)
    xl = m/(-k)
    yl = m
    print(color.BOLD +"x ass krustpunkts:" + color.END)
    print(color.GREEN + f"x = {xl}\n"+ color.END)
    print(color.BOLD + "y ass krustpunkts:" + color.END)
    print(color.GREEN + f"y = {yl}\n" + color.END)
    time.sleep(0.5)
    opt_l()
    

def lin_3():
    cls()
    print(color.GREEN + f"""D(f) = (-∞;+∞)\nE(f) = [-∞;+∞)\n""" + color.END)
    print(color.BOLD + "\n*** lineāras funkcijas definīcijas un vērtības apgabals ir visi reālie skaitļi\n" + color.END)
    time.sleep(0.5)
    opt_l()

def lin_4():
    cls()
    print(color.GREEN + "------------Divu lineāru funkciju krustpunkti------------\n" + color.END)

    print(color.GREEN + "\nIevadi otrās lineārās funkcijas vērtības\n" + color.END)
    print("""* y = kx + m
      ^
  Šī vērtība
                """)
    k2 = float(input(color.BOLD + "\nIevadi funkcijas k vertību:" + color.END))
    cls()
    print(color.GREEN + "\nIevadi otrās lineārās funkcijas vērtības\n" + color.END)
    print(color.GREEN + "------------Divu lineāru funkciju krustpunkti------------\n" + color.END)
    print("""* y = kx + m
           ^
       Šī vērtība
                """)
    m2 = float(input(color.BOLD + "\nIevadi funkcijas m vertību:" + color.END))
    cls()
    
    xi = (m2-m)/(k-k2)
    yi = (k*xi+m)

    print(color.GREEN + "------------Divu lineāru funkciju krustpunkti------------\n" + color.END)
    print(color.BOLD + "Krustpunkta kordenātes:" + color.END)
    print(color.GREEN + f"({xi};{yi})" + color.END)

    if xi == yi:
        cls()
        print(color.GREEN + "------------Divu lineāru funkciju krustpunkti------------\n" + color.END)
        print(color.BOLD + "\n Funkcijas abas ir paralēlas:" + color.END)
        print(color.GREEN + "Nav krustpunktu (lineāras funkcijas nekrustojās)" + color.END)
        opt_l()

sakums()