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
		if self.head is None:
			return False
		else:	
			val = self.head.data
			self.head = self.head.next
			return val

	def get_top_element(self):
		if self.head is None:
			return 0
		else:
			return self.head.data
		
	def print_list(self):
		temp = self.head
		while(temp):
			if temp.data is not None:
				print(temp.data)
			temp = temp.next
		print()	

	def make_empty(self):
		temp = self.head
		while(temp):
			temp.data = None
			temp = temp.next
		
		self.head = None


def infix_to_postfix(infix):
	for term in infix:
		if term.isalpha():
			print(term)
		else:
			if term=='+' or term=='-':
				top = stack.get_top_element()
				while top=='+' or top=='-' or top=='*' or top=='/' or top=='^' and top!='(':
					stack.pop()
				stack.push(term)
			
			elif term=='/' or term=='*':
				top = stack.get_top_element()
				while top=='*' or top=='/' or top=='^' and top!='(':
					stack.pop()
				stack.push(term)				

			elif term=='^' or term=='(' or term==')':
				stack.push(term)	
	
	print(stack.print_list())	


print("------------------------------INFIX TO POSTFIX------------------------------\n")		

infix_exp = input("Enter the Infix Expression: ")

stack = LinkedList()

print()

infix_to_postfix(infix_exp)