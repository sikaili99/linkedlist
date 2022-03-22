class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def print_list(self):
    if self.head is None:
      print("Empty LinkedList")
      return

    itr = self.head
    lstr = " "

    while itr:
      lstr += f"{itr.data}--->"
      itr = itr.next
    print(lstr)

llist = LinkedList()

llist.insert_at_beginning(4)
llist.insert_at_beginning(5)

llist.print_list()