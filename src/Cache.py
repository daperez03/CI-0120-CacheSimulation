from Memory import Memory
from TLB import TLB
import math

class Cache(Memory):
    def __init__(self, name:str, size:int, wordSize:int, nextMemoryLevel:"Memory"):
        super().__init__(name, size, wordSize, nextMemoryLevel)
        self.TLB = TLB(int(size/wordSize))

    def Read(self, page) -> bytearray:
        physicalPage = self.TLB.Lookup(page)
        data:bytearray
        if (physicalPage != None):
            data = self.ReadPage(physicalPage)
        else:
            data = self.nextMemoryLevel.Read(page)
            self.Write(page, data)
        return data

    def Write(self, page:int, data:bytearray):
        physicalPage, previusPage = self.TLB.AddEntry(page)
        if (previusPage != None):
            data = self.ReadPage(physicalPage)
            self.nextMemoryLevel.Write(previusPage, data)
        self.WritePage(physicalPage, data)