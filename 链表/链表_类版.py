class List:
    def __init__(self):
        self.element = None
        self.next = None

    # ??????¡À¨ª??¡¤?????
    def IsEmpty(self):
        return self.next == None

    # ??????????¡¤???¡Á??¨®????????
    def IsLast(self, position):
        return position.next == None

    # ?¨¦??????????element????????????¡¤???????????¡¤??¨°¡¤???None
    def Find(self, element):
        positionList = self
        while(positionList != None and 
              positionList.element != element):
            positionList = positionList.next
        return positionList

    # ?¨¦????????????element????????????¡¤???????????¡¤??¨°¡¤???None
    def FindPrevious(self, element):
        positionList = self
        while(positionList.next != None and 
              positionList.next.element != element):
            positionList = positionList.next
        return positionList

    # ????element?¨´????????
    def Delete(self, element):
        positionList = FindPrevious(element, self)

        if IsLast(positionList, self) != True:
            tempList = positionList.next
            posisionList.next = tempList.next
            del tempList

    # ??????element??????position?¨®
    def Insert(self ,element, position):
        tempList = List()
        tempList.element = element
        tempList.next = position.next
        position.next = tempList

    # ????????¡À¨ª
    def DeleteList(self):
        positionList = self
        while(positionList.next != None):
            tempList = positionList
            positionList = positionList.next
            del tempList

    # ¡¤????¡¤????
    def Header(self):
        return self

    # ¡¤?????????????
    def First(self):
        return self.next

    # ¡¤???position?¨®??????????
    def Advance(position):
        if postion != None:
            return position.next
        return None

    # ¡¤???position????
    def Retrieve(position):
        if position != None:
            return position.element
        return None

list = List()
list.Insert(1, list.Header())

print list.next.element

