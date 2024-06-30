from abc import ABC, abstractmethod
import math

class Memory(ABC):
    def __init__(self, name:str, size:int, wordSize:int, nextMemoryLevel:"Memory" = None):
        self.name = name
        self.nextMemoryLevel = nextMemoryLevel
        self.wordSize = wordSize
        self.memory = bytearray(size * wordSize)
    
    def ReadPage(self, page:int) -> bytearray:
        data = bytearray(self.wordSize)
        address = page * self.wordSize
        for i in range(self.wordSize):
            data[i] = self.memory[address]
            address += 1
        return data

    def WritePage(self, page:int, data:bytearray):
        address = page * self.wordSize
        for i in range(self.wordSize):
            self.memory[address] =  data[i]
            address += 1

    @abstractmethod
    def Read(self, page:int, data:bytearray):
        pass
    
    @abstractmethod
    def Write(self, page:int, data:bytearray):
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
            if (index1 < len(self.memory)) :
                str += f"|\t0x{index1:x}\t|\t{self.memory[index1]:x}\t|"
            else :
                str += f"\t\t|\t\t|\n"
            if (index2 < len(self.memory)) :
                str += f"\t0x{index2:x}\t|\t{self.memory[index2]:x}\t|"
            else :
                str += f"\t\t|\t\t|\n"
            if (index3 < len(self.memory)) :
                str += f"\t0x{index3:x}\t|\t{self.memory[index3]:x}\t|\n"
            else :
                str += f"\t\t|\t\t|\n"
            index1 += 1
            index2 += 1
            index3 += 1
        str += "-" * 97 + "\n"
        return str

