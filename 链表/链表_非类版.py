class List:
    def __init__(self):
        self.element = None
        self.next = None

# Get a empty List.
def MakeEmpty(list):
    list = List()
    return list

# Judge whether the list is empty.
def IsEmpty(list):
    return list.next == None

# Judge whether the position is last.
def IsLast(position, list):
    return position.next == None

# To find the value of element node.
def Find(element, list):
    positionList = list
    while(positionList != None and 
          positionList.element != element):
        positionList = positionList.next
    return positionList

# To find the value of element previous node.
def FindPrevious(element, list):
    positionList = list
    while(positionList.next != None and 
          positionList.next.element != element):
        positionList = positionList.next
    return positionList

# Delete the value of element node.
def Delete(element, list):
    positionList = List()
    positionList = FindPrevious(element, list)

    if IsLast(positionList, list) != True:
        tempList = List()
        tempList = positionList.next
        positionList.next = tempList.next
        del tempList

# Insert into after position of element.
def Insert(element, list, position):
    tempList = List()
    tempList.element = element
    tempList.next = position.next
    position.next = tempList

# Delete all node.
def DeleteList(list):
    positionList = list
    while(positionList.next != None):
        tempList = positionList
        positionList = positionList.next
        del tempList

# Get header.
def Header(list):
    return list

# Get the First node.
def First(list):
    return list.next

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
Insert(1, list, Header(list))
print list.next.element
Delete(1, list)
print list.next