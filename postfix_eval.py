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

	def push(self, data):
		if self.head is None:
			self.head = Node(data)
		else:	
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node
		
	def pop(self):
		val = self.head.data
		self.head = self.head.next
		return val

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

print("------------------------------POSTFIX EXPRESSION EVALUATION------------------------------\n")

postfix_exp = input("Enter the postfix expression: ")

print()

stack = LinkedList()

for term in postfix_exp:
	if term.isalpha():
		val = int(input(f"Enter the value of {term}: "))
		stack.push(val)
	else:
		p = stack.pop()
		q = stack.pop()
		
		if term=='+':
			res = p+q
			stack.push(res)
		elif term=='-':
			res = q-p
			stack.push(res)
		elif term=='*':
			res = p*q
			stack.push(res)
		elif term=='/':
			res = p/q	
			stack.push(res)
		else:
			print("Invalid operator. Quitting...")
			break			

print("\nValue of expression is:")
stack.print_list()