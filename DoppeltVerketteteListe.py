class ListElement:

    def __init__ (self, content):
        self.content = content
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.start = None
        self.tail = None


    def insertBeginning(self, content):
        element = ListElement(content)
        if (self.start == None):
            self.start = element
            self.tail = element
        else:
            x = self.start
            element.next = x
            x.prev = element
            self.start = element



    def insert_end(self, content):
        element = ListElement(content)
        if(self.start == None):
            self.insertBeginning(content)
        else:
            end = self.tail
            end.next = element
            element.prev = end
            self.tail = element



    def get_length(self):
        x = self.start
        i= 0
        while (x.next != self.tail):
            x = x.next
            i = i+1
        return i+2


    def get_all(self):
        h = self.start
        if(h == None):
            print("None")
        else:
            while (h != self.tail):
                print(h.content)
                h = h.next
            h = self.tail
            print(h.content)


    def get_index(self, content):
        x = self.start
        i = 0
        while (x.content != content):
            i = i+1
            x = x.next
        print(i)


    def get_last(self):
        print(self.tail.content)

    def get_element_by_id(self, index):
        element = self.start
        if(element == None or index > self.get_length()-1):
            print("Index größer als Länge der Liste")
        else:
            i = 0
            while(i<index):
                i += 1
                element = element.next

            print(element.content)

    def delete_all(self):
        self.start = None
        self.tail = None

    def delete_by_id(self, index):
        element = self.start
        i = 0
        while(i<index):
            i = i+1
            element = element.next
        if(element.prev == None):
            self.start = element.next
            element.next.prev = None
        elif(element.next ==None):
            self.tail = element.prev
            element.prev.next = None
        else:
            element.prev.next = element.next
            element.next.prev = element.prev


    def reverse_list(self):
        #print(self.tail.content)
        #print(self.tail.prev.content)
        new_list = LinkedList()
        x = self.tail
        while(x.prev != None):
            new_list.insert_end(x.content)
            x = x.prev
        new_list.insert_end(self.start.content)
        new_list.get_all()




def main():
    Llist = LinkedList()
    Llist.insertBeginning(1)
    Llist.insert_end(88)
    Llist.insert_end(5)
    Llist.insertBeginning(16)

    print("komplette Liste:")
    Llist.get_all()

    print("Letztes Element")
    Llist.get_last()

    print("Index eines elements")
    Llist.get_index(5)

    print("element eines Index:")
    Llist.get_element_by_id(3)

    print("element löschen mit index")
    Llist.delete_by_id(2)
    Llist.get_all()

    print("Alle Elemente der Liste tauschen")
    Llist.reverse_list()

    print("Länge der Liste")
    print(Llist.get_length())


    print("Liste löschen")
    Llist.delete_all()
    Llist.get_all()




if __name__ == "__main__":
    main()

