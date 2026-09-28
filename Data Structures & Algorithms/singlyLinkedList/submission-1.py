class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        count = 0
        current = self.head
        while current:
            if count == index:
                return current.val
            current = current.next
            
            count += 1
        return -1
        


    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        current = self.head
        if self.head is None:
            return

        while current.next:
            current = current.next
        current.next = new_node
            
        

    def remove(self, index: int) -> bool:
        count = 0
        previous = None
        current = self.head
        if self.head is None:
            return False
        while current:
            if count == index:
                if previous == None:
                    self.head = self.head.next
                    
                else:
                    previous.next = current.next
                return True        
            previous = current
            current = current.next
            count += 1
        return False

    def getValues(self) -> List[int]:
        current = self.head
        count = 0
        if current is None:
            return []
        while current:
            count += 1
            current = current.next
            
        new_arr = [0] * count
        i = 0
        current = self.head
        while current:
            new_arr[i] = current.val
            current = current.next
            i += 1
        return new_arr

