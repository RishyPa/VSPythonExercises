class List:
    def __init__(self):
        self.element = None
        self.next = None

    # Judge whether the list is empty.
    def IsEmpty(self):
        return self.next == None

    # Judge whether the position is last.
    def IsLast(self, position):
        return position.next == None

    # To find the value of element node.
    def Find(self, element):
        positionList = List()
        positionList = self
        while(positionList != None and 
              positionList.element != element):
            positionList = positionList.next
        return positionList

    # To find the value of element previous node.
    def FindPrevious(self, element):
        positionList = List()
        positionList = self
        while(positionList.next != None and 
              positionList.next.element != element):
            positionList = positionList.next
        return positionList

    # Delete the value of element node.
    def Delete(self, element):
        positionList = List()
        positionList = self.FindPrevious(element)

        if self.IsLast(positionList) != True:
            tempList = List()
            tempList = positionList.next
            positionList.next = tempList.next
            del tempList

    # Insert into after position of element.
    def Insert(self ,element, position):
        tempList = List()
        tempList.element = element
        tempList.next = position.next
        position.next = tempList

    # Delete all node.
    def DeleteList(self):
        positionList = List()
        positionList = self
        while(positionList.next != None):
            tempList = List()
            tempList = positionList
            positionList = positionList.next
            del tempList

    # Get header.
    def Header(self):
        return self

    # Get the First node.
    def First(self):
        return self.next

    # Get next of position.
    def Advance(position):
        if postion != None:
            return position.next
        return None

    # Get next value of position.
    def Retrieve(position):
        if position != None:
            return position.element
        return None

list = List()
list.Insert(1, list.Header())
print list.next.element
position = list.Find(1)
print position.element
position = list.FindPrevious(1)
print position.next.element
list.Delete(1)
print list.next