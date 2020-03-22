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

	def insert_node(self, prev, data):
		if prev is None:
			print("No node")
		else:
			new_node = Node(data)
			new_node.next = prev.next
			prev.next = new_node
		
		print("List after insertion")
		self.print_list()

	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node

		last = self.head

		while (last.next):
			last = last.next

		last.next = new_node

		print("List after appending")

		self.print_list()						

	def delete_node(self, item):
		temp = self.head
		prev_new = None
		
		if self.head.data==item:
			self.head = self.head.next
		else:	
			while(temp):
				if temp.data == item:
					prev_new.next = temp.next
					temp = None
					break
				prev_new = temp
				temp = temp.next

		print("List after deletion")
		self.print_list()			
	
	def print_list(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
		print()	

	def pop(self):
		self.head = self.head.next
		print("List after popping")
		self.print_list()

	def make_empty(self):
		temp = self.head
		while(temp):
			temp.data = None
			temp = temp.next
		
		self.head = None
		print("List emptied\n")

print("-----------------------------LINKED LIST-----------------------------\n")

linked_list = LinkedList()

while True:
	print("1. Create\n2. Push\n3. Append\n4. Delete node\n5. Pop\n6. Insert after\n7. Empty\n8. Display elements\n9. Exit")

	choice = int(input("Enter your choice: "))

	if choice == 1:	
		val  = int(input("Enter the data: "))
		linked_list.create(val)

	elif choice == 2:
		val  = int(input("Enter the data to push: "))
		linked_list.push(val)

	elif choice == 3:
		val  = int(input("Enter the data to append: "))
		linked_list.append(val)

	elif choice == 4:
		val  = int(input("Enter the data to delete: "))
		linked_list.delete_node(val)

	elif choice == 5:
		linked_list.pop()	

	elif choice == 6:
		val  = int(input("Enter the data to insert: "))
		linked_list.insert_node(linked_list.head.next, val)
	
	elif choice == 7:
		linked_list.make_empty()		

	elif choice == 8:
		print("List elements are")
		linked_list.print_list()

	elif choice == 9:
		break

	else:
		print("Enter a valid choice. Try again...")

exit()				