class ListElement:

    def __init__ (self, content):
        self.content = content
        self.next = None



class LinkedList:

    def __init__(self):
        self.start = None


    def insertBeginning(self, content):
        element = ListElement(content)
        element.next = self.start
        self.start = element



    def insert_end(self, content):
        if(self.start == None):
            self.insertBeginning(content)
        else:
            x = self.start
            while (x.next != None):
                x = x.next
            element = ListElement(content)
            x.next = element


    def get_length(self):
        x = self.start
        while (x.next != None):
            x = x.next
            i = i+1
        return i

    def get_all(self):
        h = self.start
        while (h != None):
            print(h.content)
            h = h.next


    def get_index(self, content):
        x = self.start
        i = 0
        while (x.content != content):
            i = i+1
            x = x.next
        print(i)


    def delete(self, content):

        x = self.start
        if (content == self.start.content):
            x = x.next
            while(x.next != None):
                print(x.content)
                x = x.next
            print(x.content)

        else:
                while (x.next != None):
                    a = x
                    if (x.next.content == content):
                        if (x.next.next != None):
                            x.next = x.next.next
                            x = x.next
                        else:
                            x.next = None

                    else:
                        x = x.next
                    print(a.content)

                if(a.content != x.content):
                 print(x.content)


def main():
    Llist = LinkedList()
    Llist.insertBeginning(1)
    Llist.insertBeginning(2)
    Llist.insertBeginning(3)
    Llist.insert_end(88)
    Llist.get_all()
    print()
    Llist.get_index(1)
    print()
    Llist.delete(1)



if __name__ == "__main__":
    main()

