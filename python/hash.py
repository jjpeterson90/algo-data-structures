class HashTable:
  def __init__(self, number_of_buckets):
    # self.number_of_buckets = number_of_buckets
    # self.table = [None] * self.number_of_buckets
    self.number_of_buckets = 30
    self.table = [None] * self.number_of_buckets
    
    pass

  def hash(self, key):
    # here is where you'll turn your 'value' into a hash value that will return the index of your table to insert value
    # IMPORTANT: Think about how you'd store values into the same index
    hash = 0
    for i in range(len(key)):
      hash += key.charCodeAt(i)
    return hash % len(self.table)

  def set(self, key, value):
    # here is where you'll perform your logic to insert the value into your table
    # you'll also call your hash method here to get the index where you'll store the value
    index = self.hash(key)
    self.table[index].append([key,value])

  def get(self, key):
    # here is where you'll retreive your value from the hash table
    # IMPORTANT: Think about how you'd retreive a value that from an index that has multiple values
    index = self.hash(key)
    for data in self.table[index]:
      if data[0] == key:
        return data[1]

  def has_key(self, value):
    # here is where you'll return a True or False value if there is a value stored at a specific index in your HashTable
    
    pass