class Queue(object):
    """ This is a Queue data structure implemented with a python list.
    To be specific this is  Circular Queue.
    """
    
    def __init__(self, size):
        self.__maxSize = size #Max size of queue
        self.__que = [None] * size # Queue array
        self.__front = 1 # Front of queue array
        self.__rear = 0  # Back end of queue array
        self.__nItems = 0 # Number of items in the queue
    
    def insert(self, item):
        if self.isFull(): #Check if the queue is full
            raise Exception("Queue overflow") # Raise a 'queue overflow' exceptionj
        self.__rear += 1 #Increase the rear by 1
        if self.__rear == self.__maxSize: #If the rear is equal to the max size 
            self.__rear = 0  #Set the rear to 0
        self.__que[self.__rear] = item #Set item to rear of queue
        self.__nItems += 1 #Increase the number of items by 1
        return True #return True to confirm status of insertion
    
    def remove(self):
        if self.isEmpty(): #If queue is empty
            raise Exception("Queue underflow") #Raise a 'queue underflow' exception
        front = self.__que[self.__front] #create temporary variable to store the front element to be dequeued
        self.__que[self.__front] = None # Set the front element to be dequeued to None
        self.__front += 1 # Increase the index of the fron by 1
        if self.__front == self.__maxSize: #If the front is uqual to the size of the queue
            self.__front = 0 # set the front to zero
        self.__nItems -= 1 # Reduce the number of items by 1
        return front #return the dequeued value
    
    def isFull(self):
        return self.__nItems == self.__maxSize #if the number of items is equal to the maximum size of the queue
    
    def isEmpty(self):
        return self.__nItems == 0 #If the number of items is equal to 0
    
    def peek(self):
        return None if  self.isEmpty() else self.__que[self.__front] #If the queue is empty return None else return the front element
    
    def __len__(self):
        return self.__nItems #return the number of items in the array
    
    def __str__(self):
        ans = '['
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += "]"
        return ans
    
if __name__ == "__main__":
    queue = Queue(10)
    
    for person in ["Don", "Ken", "Ivan", "Raj", "Amir", "Adi"]:
        queue.insert(person)
        
    print("After inserting", len(queue), 'persons on the queue, it contains:\n', queue)
    print("Is queue full?", queue.isFull())
    
    print("Removing items from the queue:")
    while not queue.isEmpty():
        print(queue.remove(), end=' ')
    print()
