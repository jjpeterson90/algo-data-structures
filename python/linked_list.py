
class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  
  def __init__(self):
    self.head = None
    self.length = 0


  def add(self, data):
    # How to change previous node's pointer when a new node is added?
    if self.length == 0:
      self.head = Node(data)
      self.length += 1
    else:
      current_node = self.head
    
      while current_node.next != None:
        current_node = current_node.next

      current_node.next = Node(data)
      self.length += 1


  def remove(self, data):
    previous_node = self.head
    node_to_delete = self.get(data)
    
    while previous_node.next.data != data:
      previous_node = previous_node.next
    
    if node_to_delete.next != None:
      previous_node.next = node_to_delete.next
    else:
      del node_to_delete
    self.length -= 1
      

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    current_node = self.head
    
    while current_node.data != element_to_get:
      current_node = current_node.next
      print(current_node.data)
      if current_node.next == None:
        if current_node.data != element_to_get:
          return "That node does not exist"
        return current_node
    return current_node


# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  
  def __init__(self, data):
    self.data = data
    self.next = None
  



List = LinkList()

List.add('A')
List.add('B')
List.add('C')
List.add('D')
List.add('E')

List.get('E')

List.remove('D')
print("\n")

List.get('E')
