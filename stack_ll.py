class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def create(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			print("List not empty")

		print("List after creation")
		self.print_list()		

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		print("List after pushing")	
		self.print_list()
		
	def pop(self):
		self.head = self.head.next
		print("List after popping")
		self.print_list()

	def get_top_element(self):
		print(f"Top element is {self.head.data}\n")
		
	def print_list(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
		print()	

	def make_empty(self):
		temp = self.head
		while(temp):
			temp.data = None
			temp = temp.next
		
		self.head = None
		print("List emptied\n")	

print("-----------------------------STACK USING LINKED LIST-----------------------------\n")

linked_list = LinkedList()

while True:
	print("1. Create\n2. Push\n3. Pop\n4. Display top element\n5. Display all elements\n6. Empty\n7. Exit")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		val  = int(input("Enter the data: "))
		linked_list.create(val)

	elif choice == 2:
		val  = int(input("Enter the data to push: "))
		linked_list.push(val)

	elif choice == 3:
		linked_list.pop()

	elif choice == 4:
		linked_list.get_top_element()

	elif choice == 5:
		print("Elements in the list")
		linked_list.print_list()

	elif choice == 6:
		linked_list.make_empty()

	elif choice == 7:
		break

	else:
		print("Enter a valid choice. Try again...")		

exit()			