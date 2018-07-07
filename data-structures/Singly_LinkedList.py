class Node:
	def __init__(self, val):
		self.data=val
		self.next=None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,val):
		self.data=val

	def setNext(self,val):
		self.next=val

class LinkedList:
	def __init__(self):
		self.head=None

	def isEmpty(self):
		"""Check if the list is empty"""
		return self.head is None

	def add(self,item):
		"""Add the item to the list"""
		new_node=Node(item)
		new_node.setNext(self.head)

	def size(self):
		"""Return the length/size of the list"""
		count=0
		current=self.head
		while current is not None:
			count+=1
			current=current.getNext()
		return count

	def search(self,item):
		"""Search for item in the list.If found,return True. If not found, return False"""
		current=self.head
		found=False
		while current is not None and not found:
			if current.getData() is item:
				found=True
			else:
				current=current.getNext()
		return found
	def remove(self,item):
		"""Remove item from list. If item is not found in the list, raise ValueError"""
		current=self.head
		previous=None
		found=False
		while current is not None and not found:
			if current.getData() is item:
				found=True
			else:
				previous=current
				current=current.getNext()
		if found:
			if previous is None:
				self.head=current.getNext()
			else:
				previous.setNext(current.getNext())
		else:
			raise ValueError
			print('Value not found')

	def insert(self,position,item):
		"""Insert item at position specified. If position specified is out of bounds, raise IndexError"""
		if position>self.size-1:
			raise IndexError
			print('Index out of bound')
		current=self.head
		previous=None
		pos=0
		if position is 0:
			self.add(item)
		else:
			new_head=Node(item)
			while pos<position:
				pos+=1
				previous=current.getNext()
			previous.setNext(new_node)
			new_node.setNext(current)

	def index(self,item):
		"""Return the index where item is found.If item is not found, return None"""
		current=self.head
		pos=0
		found=False
		while current is not None and not found:
			if current.getData() is item:
				found=True
			else:
				current=current.getNext()
				pos+=1
		if found:
			pass
		else:
			pos=None
		return pos

	def pop(self,position=None):
		"""
		If no arrgument is provided, return and remove the item at the head.
		If position is provided, return and remove the item at that position.
		If index is out of bounds, raise IndexError
		"""
		if position>self.size():
			print('Index out of bounds')
			raise IndexError
		current=self.head
		if position is None:
			ret=current.getData()
			self.head=current.getNext()
		else:
			pos=0
			previous=None
			while pos<position:
				previous=current
				current=current.getNext()
				pos+=1
				ret=current.getData()
			previous.setNext(current.getNext())
		print(ret)
		return ret

	def append(self,item):
		"""Append item to the end of the list"""
		current=self.head
		previous=None
		pos=0
		length=self.size()
		while pos<length:
			previous=current
			current=current.getNext()
			pos+=1
		new_node=Node(item)
		if previous is None:
			new_node.setNext(current)
			self.head=new_node
		else:
			previous.setNext(new_node)

	def printList(self):
		"""Print the list"""
		current=self.head
		while current is not None:
			print(current.getData())
			current=current.getNext()
