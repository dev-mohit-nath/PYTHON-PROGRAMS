from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fromm, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fromm} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
        
    def getFare(self, fromm, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fromm} to {to} is {randint(555, 52500)}")
        
t = Train(12345)
t.book("bhinmal","baroda")
t.getStatus()
t.getFare("bhinmal","baroda")