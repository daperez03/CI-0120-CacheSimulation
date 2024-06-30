from Memory import Memory
from TLB import TLB

class Cache(Memory):
    def __init__(self, name:str, size:int, wordSize:int, nextMemoryLevel:Memory):
        super().__init__(name, size, wordSize, nextMemoryLevel)
        self.TLB = TLB(size)

    def Read(self, page) -> bytearray:
        physicalPage = self.TLB.Lookup(page)
        data:bytearray
        # Si la pagina existe, se lee
        if (physicalPage != None):
            data = self.ReadPage(physicalPage)
        else:  # Si no, se busca en el siguiente nivel de memoria
            data = self.nextMemoryLevel.Read(page)
            self.Write(page, data)
        return data

    def Write(self, page:int, data:bytearray):
        physicalPage = self.TLB.Lookup(page)
        if (physicalPage == None):
            print("physicalPage is None")
            # previousPage es la pagina que sale para escribir la nueva
            physicalPage, previousPage = self.TLB.AddEntry(page)
            if (previousPage != None):
                print("previousPage is not None")
                # si se saco una pagina, se escribe en el proximo nivel
                previousData = self.ReadPage(physicalPage)
                self.nextMemoryLevel.Write(previousPage, previousData)
        # Si la pagina ya existe, se escribe directo
        self.WritePage(physicalPage, data)