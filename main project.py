import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.right = None
        self.left = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete_at_start(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Node(data)
            current.next.next = self.head

    def delete_at_start(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if self.head:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next.next != self.head:
                    current = current.next
                current.next = self.head

    def display(self):
        if self.head:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
        print()

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

class Queue:
    def __init__(self, size=1000):
        self.q = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

    def dequeue(self):
        if self.is_empty():
            print('Queue Underflow!! Terminating process.')
            exit(-1)
        x = self.q[self.front]
        print('Removing element…', x)
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return x

    def enqueue(self, value):
        if self.is_full():
            print('Overflow!! Terminating process.')
            exit(-1)
        print('Inserting element…', value)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count += 1

    def peek(self):
        if self.is_empty():
            print('Queue UnderFlow!! Terminating process.')
            exit(-1)
        return self.q[self.front]

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def display(self):
        print("Queue: ", end="")
        for i in range(self.count):
            print(self.q[(self.front + i) % self.capacity], end=" ")
        print()

class Graphs:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            print(f"One or both vertices not found in graph. Add vertices before adding edges.")
        else:
            self.graph[vertex1].append((vertex2, weight))
            self.graph[vertex2].append((vertex1, weight))

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)

class Sorting:
    def __init__(self):
        self.arr = []

    def bubble_sort(self):
        arr = self.arr.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    def insertion_sort(self):
        arr = self.arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def get_user_input(self):
        user_input = input("Enter numbers separated by spaces: ")
        self.arr = [int(x) for x in user_input.split()]
        print(f"List of numbers: {self.arr}")

# Create instances of classes
linked_list = SLinkedList()
circular_linked_list = CircularLinkedList()
stack_ds = Stack()
queue_ds = Queue()
graph_ds = Graphs()
binary_tree_ds = BinaryTree()
sorting_ds = Sorting()

while True:
    print("\nMain Menu:")
    print("1. Linked List")
    print("2. Circular Linked List")
    print("3. Stack")
    print("4. Queue")
    print("5. Graph")
    print("6. Binary Tree")
    print("7. Sorting")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\nLinked List Menu:")
            print("1. Insert at Start")
            print("2. Insert at End")
            print("3. Delete at Start")
            print("4. Delete at End")
            print("5. Display")
            print("6. Back to Main Menu")

            ll_choice = input("Enter your choice: ")

            if ll_choice == '1':
                data = int(input("Enter data to insert at start: "))
                linked_list.insert_at_start(data)
            elif ll_choice == '2':
                data = int(input("Enter data to insert at end: "))
                linked_list.insert_at_end(data)
            elif ll_choice == '3':
                linked_list.delete_at_start()
            elif ll_choice == '4':
                linked_list.delete_at_end()
            elif ll_choice == '5':
                linked_list.display()
            elif ll_choice == '6':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '2':
        while True:
            print("\nCircular Linked List Menu:")
            print("1. Insert at Start")
            print("2. Insert at End")
            print("3. Delete at Start")
            print("4. Delete at End")
            print("5. Display")
            print("6. Back to Main Menu")

            cll_choice = input("Enter your choice: ")

            if cll_choice == '1':
                data = int(input("Enter data to insert at start: "))
                circular_linked_list.insert_at_start(data)
            elif cll_choice == '2':
                data = int(input("Enter data to insert at end: "))
                circular_linked_list.insert_at_end(data)
            elif cll_choice == '3':
                circular_linked_list.delete_at_start()
            elif cll_choice == '4':
                circular_linked_list.delete_at_end()
            elif cll_choice == '5':
                circular_linked_list.display()
            elif cll_choice == '6':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '3':
        while True:
            print("\nStack Menu:")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            stack_choice = input("Enter your choice: ")

            if stack_choice == '1':
                data = int(input("Enter data to push: "))
                stack_ds.push(data)
            elif stack_choice == '2':
                print("Popped data:", stack_ds.pop())
            elif stack_choice == '3':
                print("Peeked data:", stack_ds.peek())
            elif stack_choice == '4':
                stack_ds.display()
            elif stack_choice == '5':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '4':
        while True:
            print("\nQueue Menu:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back to Main Menu")

            queue_choice = input("Enter your choice: ")

            if queue_choice == '1':
                data = int(input("Enter data to enqueue: "))
                queue_ds.enqueue(data)
            elif queue_choice == '2':
                print("Dequeued data:", queue_ds.dequeue())
            elif queue_choice == '3':
                print("Peeked data:", queue_ds.peek())
            elif queue_choice == '4':
                queue_ds.display()
            elif queue_choice == '5':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '5':
        while True:
            print("\nGraph Menu:")
            print("1. Add Vertex")
            print("2. Add Edge")
            print("3. Display")
            print("4. Dijkstra's Algorithm")
            print("5. Back to Main Menu")

            graph_choice = input("Enter your choice: ")

            if graph_choice == '1':
                vertex = input("Enter vertex to add: ")
                graph_ds.add_vertex(vertex)
            elif graph_choice == '2':
                vertex1 = input("Enter first vertex: ")
                vertex2 = input("Enter second vertex: ")
                weight = int(input("Enter edge weight: "))
                graph_ds.add_edge(vertex1, vertex2, weight)
            elif graph_choice == '3':
                graph_ds.display()
            elif graph_choice == '4':
                start_vertex = input("Enter start vertex: ")
                distances = graph_ds.dijkstra(start_vertex)
                print("Shortest paths from", start_vertex, ":", distances)
            elif graph_choice == '5':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '6':
        while True:
            print("\nBinary Tree Menu:")
            print("1. Insert")
            print("2. Inorder Traversal")
            print("3. Preorder Traversal")
            print("4. Postorder Traversal")
            print("5. Back to Main Menu")

            bt_choice = input("Enter your choice: ")

            if bt_choice == '1':
                data = int(input("Enter data to insert: "))
                binary_tree_ds.insert(data)
            elif bt_choice == '2':
                result = []
                binary_tree_ds.inorder_traversal(binary_tree_ds.root, result)
                print("Inorder Traversal:", result)
            elif bt_choice == '3':
                result = []
                binary_tree_ds.preorder_traversal(binary_tree_ds.root, result)
                print("Preorder Traversal:", result)
            elif bt_choice == '4':
                result = []
                binary_tree_ds.postorder_traversal(binary_tree_ds.root, result)
                print("Postorder Traversal:", result)
            elif bt_choice == '5':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '7':
        while True:
            print("\nSorting Menu:")
            print("1. Enter List")
            print("2. Bubble Sort")
            print("3. Insertion Sort")
            print("4. Back to Main Menu")

            sort_choice = input("Enter your choice: ")

            if sort_choice == '1':
                sorting_ds.get_user_input()
            elif sort_choice == '2':
                sorted_arr = sorting_ds.bubble_sort()
                print("Sorted List (Bubble Sort):", sorted_arr)
            elif sort_choice == '3':
                sorted_arr = sorting_ds.insertion_sort()
                print("Sorted List (Insertion Sort):", sorted_arr)
            elif sort_choice == '4':
                break
            else:
                print("Invalid choice! Please enter again.")

    elif choice == '8':
        print("code exited")
        break

    else:
        print("Invalid choice! Please enter again.")
