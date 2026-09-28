class DynamicArray:
    
    def __init__(self, capacity: int):
        len(list) == capacity

    def get(self, i: int) -> int:
        for j in range(len(mylist)):
            if j == i:
                return mylist[j]
            else:
                continue

    def set(self, i: int, n: int) -> None:
        for j in range(len(mylist)):
            if j == i:
                mylist[j] == n
            else:
                continue

    def pushback(self, n: int) -> None:
        if mylist[-1] == null:
            mylist.append(n)
        else:
            len(mylist) == len(mylist) * 2

    def popback(self) -> int:
        h = mylist.pop(-1)
        return h

    def resize(self) -> None:
        len(mylist) == len(mylist) * 2

    def getSize(self) -> int:
        count = 0
        for i in range(len(mylist)):
            if mylist[i] == null:
                return count
            else:
                count+=1
    
    def getCapacity(self) -> int:
        counter = 0
        for i in range(len(mylist)):
            counter+=1
        return counter
