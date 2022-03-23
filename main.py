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

  def insert_at(self, index, data):
    if index < 0 or index > self.get_length():
      raise Exception("Error invalid index provided.")
      return None

    if index == 0:
      self.insert_at_beginning(data)
      return None
    itr = self.head
    count = 0
    while itr:
      if count == index - 1:
        node = Node(data, itr.next)
        itr.next = node
        break
        
      itr = itr.next
      count += 1

  def insert_values(self, values):
    for value in values:
      self.insert_at_beginning(value)
    return

  def get_length(self):
    itr = self.head
    count = 0

    while itr:
      itr = itr.next
      count += 1
    return count

  def remove_at(self, index):
    if index < 0 or index > self.get_length():
      raise Exception("Error invalid index provided.")
      return None
      
    if index == 0:
      self.head = self.head.next
      return None
      
    itr = self.head
    count = 0

    while itr:

      if count == index - 1:
        itr.next = itr.next.next
        break
        
      itr = itr.next
    return None

  def print_list(self):
    if self.head is None:
      print("Empty LinkedList")
      return None

    itr = self.head
    lstr = ""

    while itr:
      lstr += f"{itr.data}--->"
      itr = itr.next
    print(lstr)

if __name__ == "__main__":
  llist = LinkedList()
  
  llist.insert_values([8,9,8,5,7,76,12,65454])
  llist.insert_at_end(6543)
  llist.insert_at(1,40)
  # llist.remove_at(0)
  
  llist.print_list()
  