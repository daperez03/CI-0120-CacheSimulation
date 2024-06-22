from abc import ABC, abstractmethod
import math

class Memory(ABC):
    def __init__(self, name:str, capacity:int, wordSize:int, nextMemoryLevel:"Memory" = None):
        self.name = name
        self.nextMemoryLevel = nextMemoryLevel
        self.wordSize = wordSize
        self.memory = bytearray(capacity)
    
    @abstractmethod
    def read(self, address) -> bytearray:
        pass

    @abstractmethod
    def write(self, address:int, data:bytearray):
        pass

    def __str__(self):
        str = "-" * 97 + "\n"
        str += f"\t\t\t\t\t{self.name}\n"
        str += "-" * 97 + "\n"
        str += "|    Address    |    Content    |    Address    |    Content    |    Address    |    Content    |\n"
        block = math.ceil(len(self.memory)/3)
        index1 = 0
        index2 = block
        index3 = 2 * block
        for i in range(block):
            str += f"|\t0x{index1:x}\t|\t{self.memory[index1]:x}\t|"
            str += f"\t0x{index2:x}\t|\t{self.memory[index2]:x}\t|"
            if (index3 < len(self.memory)) :
                str += f"\t0x{index3:x}\t|\t{self.memory[index3]:x}\t|\n"
            else :
                str += f"\t\t|\t\t|\n"
            index1 += 1
            index2 += 1
            index3 += 1
        str += "-" * 97 + "\n"
        return str

