class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node 
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next =Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    
    def print_linkedlist(self):
        if self.head is None:
            print("Linkedlist is empty")
            return 
        itr = self.head
        list_str = ''
        while itr:
            list_str+=str(itr.data)+ '-->'
            itr = itr.next
        print(list_str)

if __name__ == '__main__':
    mylist = Linkedlist()
    # mylist.insert_at_begining(2)
    # mylist.insert_at_begining(3)
    # mylist.insert_at_begining(4)
    # mylist.insert_at_begining(5)
    # mylist.insert_at_end(10)
    mylist.insert_values([2,3,4,5])
    mylist.print_linkedlist()