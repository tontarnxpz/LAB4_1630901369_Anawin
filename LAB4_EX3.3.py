class node:
    def __init__(self,val):
        self.prv = None
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        newNode = node(val)
        if self.head == None:
            self.head = newNode
        else:
            poin = self.head
            while poin.next is not None:
                poin = poin.next
            poin.next = newNode
            newNode.prv = poin

    def display(self):
        displayVal = self.head
        print("header -> ", end="")
        while displayVal is not None:
            print(displayVal.val, end="")
            displayVal = displayVal.next
            if displayVal is not None:
                print(" -> ", end="")
            else:
                print("")

if __name__ == "__main__":
    List = linkedList()

    List.push(104)
    List.push(44)
    List.push(36)
    List.push(90)
    List.push(10)
    List.push(60)
    List.push(99)

inPush = input("Enter the number you want to Insert : ")
List.push(inPush)
List.display()