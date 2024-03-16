class Queue(object):
    
    def __init__(self):
        """ This class implements a queue with 2 stacks.
        The main methods here will be enqueue and dequeue
        """
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, val):
        self.stack2.append(val)
        
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise Exception("Cannot dequeue from empty stacks!")
        
        if not self.stack1 and self.stack2:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
                
        return self.stack1.pop()
    
def test_queue():
    # Test case 1: Enqueue operation
    q = Queue()
    q.enqueue(1)
    assert q.stack2 == [1], "Test Case 1 Failed"
    
    # Test case 2: Multiple enqueue operations
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.stack2 == [1, 2, 3], "Test Case 2 Failed"
    
    # Test case 3: Dequeue operation after multiple enqueue operations
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1, "Test Case 3 Failed"
    
    # Test case 4: Dequeue operation on an empty queue
    q = Queue()
    try:
        q.dequeue()
    except Exception as e:
        assert str(e) == "Cannot dequeue from empty stacks!", "Test Case 4 Failed"
    
    # Test case 5: Multiple enqueue and dequeue operations
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue()
    q.enqueue(3)
    assert q.dequeue() == 2, "Test Case 5 Failed"
    
    # Test case 6: Dequeue operation until the queue is empty
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    try:
        q.dequeue()
    except Exception as e:
        assert str(e) == "Cannot dequeue from empty stacks!", "Test Case 6 Failed"
    
    print("All test cases passed")

if __name__ == "__main__":
    test_queue()


        
        
        
    