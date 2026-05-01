class DLNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size
    
    def add_first(self, data):
        new_node = DLNode(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

        return self

    def add_last(self, data):
        new_node = DLNode(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

        return self

    def delete(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                self.size -= 1
                return self
            current = current.next
        return self
    
    def print_list(self):
        current = self.head
        data = ""
        while current != None:
            data += str(current.data) + " <--> "
            current = current.next

        print(data + "None(tail)")    
        return self
    
dl_list = DoublyLinkedList()
dl_list.add_first(1).add_first(2).print_list()
dl_list.add_last(3).add_last(4).print_list()
dl_list.delete(1).print_list()
dl_list.delete(2).print_list()
dl_list.delete(3).print_list()