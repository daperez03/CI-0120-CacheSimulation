class TLB:
    def __init__(self, size):
        self.size = size
        self.entries = {}  # Mapa de Virtual Page a TLBEntry
        self.accessOrder = []  # Lista para seguir el orden de acceso
        self.availableAddresses = list(range(size))

    def Lookup(self, virtualPageNumber) -> int|None:
        if virtualPageNumber in self.entries:
            # Mover la entrada al final de la lista de acceso (LRU)
            self.accessOrder.remove(virtualPageNumber)
            self.accessOrder.append(virtualPageNumber)
            return self.entries[virtualPageNumber].physicalPageNumber
        else:
            return None

    def AddEntry(self, virtualPageNumber) -> tuple[int, int|None]:
        physicalPageNumber:int
        previusPage = None
        if len(self.entries) >= self.size:
            # Remover la entrada menos recientemente usada
            previusPage = self.accessOrder.pop(0)
            physicalPageNumber = self.entries[previusPage]
            del self.entries[previusPage]
        else:
            # obtener nueva direccion fisica
            physicalPageNumber = self.availableAddresses.pop()

        # Añadir la nueva entrada
        self.entries[virtualPageNumber] = physicalPageNumber
        self.accessOrder.append(virtualPageNumber)
        return physicalPageNumber, previusPage
    
    def __str__(self):
        return str(self.entries)