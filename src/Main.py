from RAM import RAM
from Cache import Cache
import os

MEMORY = RAM("Random Access Memory", 10, 3)
L3 = Cache("L3", 8, 3, MEMORY)
L2 = Cache("L2", 5, 3, L3)
L1 = Cache("L1", 3, 3, L2)


def Read(L1:Cache):
    os.system('cls')
    
    print("Ingrese la pagina que desea leer:")
    inpt = input()
    if not inpt.isdecimal():
        return
    page:int = int(inpt)
    data = L1.Read(page)
    print(data)

def Write(L1:Cache):
    os.system('cls')

    print("Ingrese la pagina a escribir:")
    inpt = input()
    if not inpt.isdecimal():
        return
    page:int = int(inpt)
    
    print("Ingrese el dato a escribir: ")
    inpt = input()
    if L1.wordSize != len(inpt):
        return
    data:bytearray = bytearray(inpt.encode("ascii"))

    L1.Write(page, data)

while True:
    print("\t\tMenu:\n1. Write\n2. Read\n3. Imprimir Memorias\n4. Salir")
    option = input()
    if (option.isdecimal() and int(option) > 0 and int(option) < 6):
        match int(option):
            case 1:
                Write(L1)
            case 2:
                Read(L1)
            case 3:
                os.system('cls')
                print(L1)
                print(L1.TLB)
                print()
                print(L2)
                print(L2.TLB)
                print()
                print(L3)
                print(L3.TLB)
                print()
                print(MEMORY)
            case 4:
                break
    else:
        print("Intente de nuevo")


