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

    def delete(self,val):
        poin = self.head

        while poin.val != val:
            if poin.next == None:
                break
            else:
                poin = poin.next
        if poin.next == None and poin.val != val:
            print("This option is not available")
        else:
            print("Delete number '",poin.val,"' complete")

            prevNode = poin.prv
            prevNode.next = poin.next

            prevNode.next.prv = None
            poin.next = None
            poin.prv = None

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

List.display()
inDelete = int(input("Enter the number you want to Delete : "))
List.delete(inDelete)
List.display()