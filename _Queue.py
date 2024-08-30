class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        cur_node = self.first

        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:   
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        
        self.length -= 1
        return temp
    

queue = Queue(1)
queue.enqueue(2)
queue.dequeue()
queue.print_queue()