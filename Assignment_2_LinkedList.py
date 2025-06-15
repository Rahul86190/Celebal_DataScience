class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def Traversal(self,head):
        self.head=head
        self.current_node=self.head
        while (self.current_node):
            print(self.current_node.data,end="->")
            self.current_node=self.current_node.next
        print("Null")

    def Length_of_the_list(self,head):
        self.currentnode=head
        self.length=0
        while(self.currentnode):
             self.length+=1
             self.currentnode=self.currentnode.next
        return self.length

    def deletion(self,head,position):
        self.head=head
        self.position=position
        try:
            if self.position==1:
                    return self.head.next
                
            self.currentNode=self.head
            for _ in range(1,self.position-1):
                    if self.currentNode is None:
                        break
                    self.currentNode=self.currentNode.next
            try:
                if self.currentNode.next is None:
                        print("invalid position\n")
                        return self.head
            
                
                self.currentNode.next=self.currentNode.next.next
                return self.head  
            except:
                print("Index out off range")    
                return self.head
        
        except:
            print("List is empty")

    def Insertion(self,head,new_node,position):
        try:
            self.head=head
            self.new_node=new_node
            self.position=position
            if self.position==1:
                self.new_node.next=self.head
                return self.new_node
            self.currentNode=self.head
            for _ in range(1,self.position-1):
                if self.currentNode is None:
                    break
                self.currentNode=self.currentNode.next
            self.new_node.next=self.currentNode.next
            self.currentNode.next=self.new_node
            return self.head
        except:
             print("try with valid Position")
             return self.head

node1=Node(5)
node2=Node(13)
node3=Node(24)
node4=Node(61)
node5=Node(29)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

# here linked list object is created
Linked_List_obj=LinkedList()

# Length of the linkedList
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")

# print the Linked List by traversal object
print("Linked list is given below....")
Linked_List_obj.Traversal(node1)

# Insert new node at starting
print("\nInserting New node at the starting")
new_node=Node(90)
node1=Linked_List_obj.Insertion(node1,new_node,1)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")


# Insert new node at end of the list
print("Inserting New node at the End")
new_node2=Node(95)
node1=Linked_List_obj.Insertion(node1,new_node2,7)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")


# Insert new node at any position 
print("Inserting New node at any Position. here we inserting at 3rd position")
new_node3=Node(30)
node1=Linked_List_obj.Insertion(node1,new_node3,3)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")


# Deletion form 1st position
print("Deleting starting node")
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")


# Deletion from last position
print("Deleting Last node")
node1=Linked_List_obj.deletion(node1,Linked_List_obj.Length_of_the_list(node1))
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")

# Deletion form nth position
print("Deleting nth node. Here Deleting 4th node")
node1=Linked_List_obj.deletion(node1,4)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")

# delete a node when index is out of range
print("delete a node when index is out of range")
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1))
node1=Linked_List_obj.deletion(node1,10)

# Delete a node when list is empty
# Now we are going me first empty our list. ( Lenght of linked list will be 0)
print("\nWhen deleting an Element from an empty list")
print("current list is : ")
Linked_List_obj.Traversal(node1)
print("Length of the list is - ",Linked_List_obj.Length_of_the_list(node1))
print("Now we are going to make our list empty.\n")

Linked_List_obj.Traversal(node1)
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)

print("\nNow we have Empty List")
print("When Try to deleting element form an empty list is will give result as below ")
node1=Linked_List_obj.deletion(node1,1)
Linked_List_obj.Traversal(node1)
print("Length of the list : ",Linked_List_obj.Length_of_the_list(node1))

print("\nList is empty now we can again insert values in it")
# insert Valus at potition 1
new_node=Node(90)
node1=Linked_List_obj.Insertion(node1,new_node,1)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")


# Here length of list is 1, but when we provide a jump in position then error will occur and handled by except block.
print("when we provide a jump in position")
new_node2=Node(20)
node1=Linked_List_obj.Insertion(node1,new_node,3)
print("List is as ")
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")

# inserting  at position 2
print("Insert 20 at valid position 2")
new_node3=Node(20)
node1=Linked_List_obj.Insertion(node1,new_node3,2)
Linked_List_obj.Traversal(node1)
print("Length of the Linked List is :", Linked_List_obj.Length_of_the_list(node1),"\n")