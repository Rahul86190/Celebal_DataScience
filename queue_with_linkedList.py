class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue_with_linkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.rear is None:
            self.rear=self.front=new_node
            self.size+=1
            return
        self.rear.next=new_node
        self.rear=new_node
        self.size+=1

    def isempty(self):
        return self.size==0
    
    def dequeue(self):
        if self.isempty:
            return "Queue is empty"
        
        a=self.front
        self.front=a.next
        self.size-=1

        if self.front is None:
            self.rear=None
        return f"Dequeued value is {a.value}"
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue_with_linkedList()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
# myQueue.size()
# print(f"Size: {}")