class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def create(self, data):
		self.head = Node(data)
		self.tail = self.head
		print("List after creation")
		self.print_list()

	def enque(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node
		print("List after enquing")
		self.print_list()

	def deque(self, data):
		if self.head is None:
			print("List is empty")
		else:
			new_node = self.head
			self.head = self.head.next
			new_node.next = None
		print("List after dequing")	
		self.print_list()	

	def get_latest_element(self):
		print(f"Latest element is {self.tail.data}")

	def get_last_element(self):
		print(f"Last element is {self.head.data}")

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
		self.tail = None
		print("List emptied\n")

print("-----------------------------QUEUE USING LINKED LIST-----------------------------\n")

linked_list = LinkedList()

while True:
	print("1. Create\n2. Enque\n3. Deque\n4. Display latest element\n5. Display oldest element\n6. Display all elements\n7. Empty\n8. Exit")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		val  = int(input("Enter the data: "))
		linked_list.create(val)

	elif choice == 2:
		val  = int(input("Enter the data to enque: "))
		linked_list.enque(val)

	elif choice == 3:
		linked_list.deque()

	elif choice == 4:
		linked_list.get_latest_element()

	elif choice == 5:
		linked_list.get_last_element()	

	elif choice == 6:
		print("Elements in the list")
		linked_list.print_list()

	elif choice == 7:
		linked_list.make_empty()

	elif choice == 8:
		break

	else:
		print("Enter a valid choice. Try again...")		

exit()