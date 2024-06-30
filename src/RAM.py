from Memory import Memory

class RAM(Memory):
    def __init__(self, name:str, size:int, wordSize:int, nextMemoryLevel:Memory=None):
        super().__init__(name, size, wordSize, nextMemoryLevel)

    def Read(self, page) -> bytearray:
        return self.ReadPage(page)

    def Write(self, page:int, data:bytearray):
        self.WritePage(page, data)