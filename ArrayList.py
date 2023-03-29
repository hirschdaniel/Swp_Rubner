class ArrayList():

    def __init__(self):
        self.arrayList = []


    def append(self, content):
        self.arrayList.append(content)

    def printAl(self):
        return self.arrayList


    def clear(self):
        self.arrayList.clear()

    def length(self):
        return len(self.arrayList)

    def extend(self,content):
        self.arrayList.extend(content)

    def reverse(self):
        self.arrayList.reverse()


    def pop(self, index):
        self.arrayList.pop(index)





def main():
    tempList = [1,2,3]
    aL =ArrayList()
    aL.append(3)
    aL.append(8)
    aL.append(9)
    aL.append(14)
    print(aL.printAl())
    print(aL.length())
    aL.extend(tempList)
    print(aL.printAl())
    aL.reverse()
    print(aL.printAl())
    aL.pop(2)
    print(aL.printAl())






if __name__ == "__main__":
    main()
