class SLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SList:
    def __init__(self, head=None, length=0):
        self.head = head
        self.length = length
    
    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        self.length += 1

        return self

    def remove_from_front(self):
        current_node = self.head
        if current_node == None:
            return self
        
        next_node = current_node.next
        self.head = next_node
        current_node.next = None
        self.length -= 1

        return self

    
    def print_values(self):
        runner = self.head
        result = ""
        while(runner != None):
            result += str(runner.value) + " -> "
            runner = runner.next
        
        print(result + "None", "- len:", self.length)
        return self
    
    def add_to_back(self, value):
        if self.head == None:
            self.add_to_front(value)
            
            return self

        new_node = SLNode(value)
        current_head = self.head
        while(current_head.next != None):
            current_head = current_head.next
        current_head.next = new_node
        self.length += 1

        return self
    
    def remove_from_back(self):
        currnt_node = self.head
        if (currnt_node == None):
            return self
        
        if (currnt_node.next == None):
            self.head = None
            self.length -= 1

            return self
        
        while(currnt_node.next.next != None):
            currnt_node = currnt_node.next
        
        currnt_node.next = None
        self.length -= 1

        return self
    
    def remove_val(self, value):
        current_node = self.head
        if (current_node == None):
            return self
        
        if (str(current_node.value) == str(value)):
            self.remove_from_front()
            return self
        
        if (current_node.next == None):
            return self
        
        while(current_node != None):
            if (str(current_node.next.value) == str(value)):
                current_node.next = current_node.next.next
                break
            current_node = current_node.next

        self.length -= 1

        return self
    
    def insert_at(self, value, n):
        if (n == 0):
            self.add_to_front(value)

            return self

        if (n == self.length):
            self.add_to_back(value)
            
            return self

        if(0 < n < self.length):
            current_node = self.head
            counter = 0
            while(current_node != None):
                if(n - 1 == counter):
                    new_node = SLNode(value)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    self.length += 1
                    
                current_node = current_node.next
                counter += 1

        return self


def run():
    s_list = SList()
    s_list.add_to_front(1)
    s_list.add_to_front(2)
    s_list.add_to_front(3)

    s_list.add_to_back(4)
    s_list.add_to_back(5)

    s_list.print_values()

    s_list.remove_from_front().print_values()
    s_list.remove_from_back().print_values()

    s_list.remove_val(1).print_values()
    s_list.remove_val(2).print_values()
    s_list.remove_val(5).print_values()
    s_list.remove_val(3).print_values()
    s_list.remove_val(4).print_values()
    s_list.remove_val(4).print_values()

    s_list.insert_at(10, 0).print_values()
    s_list.insert_at(9, 1).print_values()
    s_list.insert_at(8, 2).print_values()
    s_list.insert_at(7, 3).print_values()
    s_list.insert_at(6, 2).print_values()

if __name__ == "__main__":
    run()