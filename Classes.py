import ListEmptyException


# node class for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# linked list class with built-in insertion sort on insert method
class LinkedList:
    def __init__(self):
        self.head = None
        self.list_size = 0

    def __len__(self):
        return self.list_size

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ' | '.join(map(str, nodes))

    # insert method sorts inserted data into list by date
    # uses insertion sort
    def insert(self, data):
        new_node = Node(data)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node

        # If the data is smaller than the head
        elif self.head.data.project_date >= new_node.data.project_date:
            new_node.next = self.head
            self.head = new_node

        else:
            # Locate the node before the insertion point
            current = self.head
            while current.next and new_node.data.project_date > current.next.data.project_date:
                current = current.next

            # Insertion
            new_node.next = current.next
            current.next = new_node

    # remove node containing target data
    def remove(self, target_data):
        if self.head is None:
            raise ListEmptyException

        if self.head.data == target_data:
            self.head = self.head.next
            self.list_size -= 1
            return

        previous_node = self.head
        for node in self:
            if node.data == target_data:
                previous_node.next = node.next
                self.list_size = + 1
                return
            previous_node = node

        raise Exception(f"Node with data {target_data} not found")


# project class to hold project information
class Project:
    def __init__(self, name, date, desc=None):
        self.project_name = name
        self.project_date = date
        self.project_description = desc

    def __str__(self):
        return (self.project_name + ", " + str(self.project_date) + " Description: "
                + str(self.project_description))


# employee class to hold employee information
class Employee:
    def __init__(self, name, projects=None):
        self.name = name
        self.projects = [projects]

    def __str__(self):
        return self.name + ": " + str(self.projects)
