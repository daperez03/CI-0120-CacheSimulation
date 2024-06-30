from RAM import RAM
from Cache import Cache
import os

MEMORY = RAM("Random Access Memory", 30, 3)
L3 = Cache("L3", 10, 3, MEMORY)
L2 = Cache("L2", 10, 3, L3)
L1I = Cache("L1.I", 5, 3, L2)
L1M = Cache("L1.M", 5, 3, L2)

while True:
    print("\t\tMenu:\n1. Write Instruction\n2. Write Data\n3. Read\n4. Clear\n5. Salir")
    option = input()
    if (option.isdecimal() and int(option) > 0 and int(option) < 6):
        match int(option):
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                os.system('cls')
            case 5:
                break
    else:
        print("Try again")