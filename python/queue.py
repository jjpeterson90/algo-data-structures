from re import L


class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.queue = []
    self.queue_size = 0

  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.insert(0, data)
    self.queue_size += 1
    pass

  def dequeue(self):
    self.queue.pop()
    self.queue_size -= 1
    pass

  def size(self):
    # write your code that returns the size of the Queue
    pass
  
  def __str__(self):
    return f'{self.queue}'

a = Queue()

print(a)

a.enqueue('a')
a.enqueue('b')
a.enqueue('c')
print(a)

a.dequeue()
print(a)

a.enqueue('d')
a.enqueue('e')
print(a)

a.dequeue()

