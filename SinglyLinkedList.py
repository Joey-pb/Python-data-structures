class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre_node = self.head

        while(temp.next):
            pre_node = temp
            temp = temp.next

        self.tail = pre_node
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp 

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
             return None
         
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node
    
    def set_value(self, index, value):
        current_node = self.get(index)

        if current_node:
            current_node.value = value
            return True
        
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == self.length - 1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            temp = self.get(index - 1)
            current_node = temp.next
            temp.next = current_node.next
            current_node.next = None
            self.length -= 1
            return current_node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        suc_node = temp.next
        pre_node = None

        for _ in range(self.length):
            suc_node = temp.next
            temp.next = pre_node
            pre_node = temp
            temp = suc_node


    def find_middle_node(self):
            fast_pointer = self.head
            slow_pointer = self.head
            
            while fast_pointer is not None and fast_pointer.next is not None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                
            return slow_pointer.value
    