class Node:
    def __init__(self,value):
        self.value=value
        self.next_node=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next_node=self.head
        self.head=new_node
        self.size+=1

    def isempty(self):
        return self.size==0
    
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        pop_element=self.head
        self.head=self.head.next_node
        self.size-=1
        return f"'{pop_element.value}' is popped"

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        return self.head.value
    
    def size_of_stack(self):
        return self.size
    
    def stack_values(self):
        present_node=self.head
        while present_node:
            print(present_node.value,end=" --> ")
            present_node=present_node.next_node
        print("\n")

mystack=Stack()
print(mystack.peek())
print(mystack.isempty())
print(mystack.size_of_stack())
print(mystack.pop())
print()

mystack.push("saini")
mystack.push("Rahul")
mystack.push("is")
mystack.push("name")
mystack.push("My")

print("stack traversal is like -- ")
mystack.stack_values()

print(mystack.peek())
print(mystack.isempty())
print(mystack.size_of_stack())
print(mystack.pop())
print()

print("stack traversal is like -- ")
mystack.stack_values()
