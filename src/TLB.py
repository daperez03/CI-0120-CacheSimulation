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
            return self.entries[virtualPageNumber]
        else:
            return None

    def AddEntry(self, virtualPageNumber) -> tuple[int, int|None]:
        physicalPageNumber:int
        previousPage = None
        if not self.availableAddresses:
            # Remover la entrada menos recientemente usada
            previousPage = self.accessOrder.pop(0)
            physicalPageNumber = self.entries[previousPage]
            del self.entries[previousPage]
        else:
            # obtener nueva direccion fisica
            physicalPageNumber = self.availableAddresses.pop()

        # Añadir la nueva entrada
        self.entries[virtualPageNumber] = physicalPageNumber
        self.accessOrder.append(virtualPageNumber)
        return physicalPageNumber, previousPage
    
    def __str__(self):
        string = "\t\t\t\t\tTLB \n"
        string += str(self.entries)
        return string
