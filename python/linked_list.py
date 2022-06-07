from operator import index
import queue


class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self):
    node_names = 'bcdefghijklmnopqrstuvwxyz'
    self.node_names = node_names.reversed()
    self.previous_node = None
    self.name = 0
    self.head = None
    self.length = 0
    
    pass

  def add(self, data):
    # How to change previous node's pointer when a new node is added?
    new_node = Node(data)
    
    # if self.head == None:
    #   self.head = new_node
    # elif self.previous_node != None:
    #   self.previous_node = new_node
    self.length += 1
    pass

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    self.length -= 1
    pass

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    pass

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  
  def __init__(self, data):
    self.data = data
    self.next = None
  
  pass

List = LinkList()
