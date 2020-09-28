class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.Item = -1

    def append(self, item):
        if self.capacity is len(self.data):
            self.Item = (self.Item + 1) % self.capacity
            self.data[self.Item] = item
        else:
            self.data.append(item)
            self.Item += 1

    def get(self):
        return self.data
                
                

    
Buffer = RingBuffer(5)

Buffer.append(5)
Buffer.append(4)
Buffer.append(3)
Buffer.append(2)
Buffer.append(1)
Buffer.append(0)
Buffer.append(-1)



print(Buffer.get())

