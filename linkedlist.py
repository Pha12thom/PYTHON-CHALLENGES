class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to the new node

    def print_list(self):
        current_node = self.head
        while current_node:  # Traverse the list and print each node's data
            print(current_node.data)
            current_node = current_node.next

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(7)
ll.print_list()