class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return None
    
    itr = self.head

    while itr.next:
      itr = itr.next
      
    itr.next = Node(data, None)

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

if __name__ == "__main__":
  llist = LinkedList()

  llist.insert_at_beginning(8)
  llist.insert_at_beginning(9)
  llist.insert_at_beginning(10)
  llist.insert_at_beginning(11)
  llist.insert_at_end(7)
  
  
  llist.print_list()