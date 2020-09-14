class Coke():
    def __init__(self,capacity):
        self.capacity = capacity
        self.amount = 0
    

    def fill(self):
        self.amount = self.capacity

    def empty(self):    
        self.amount = 0

    def refill(self, amount):
        self.amount +=amount
        if(self.amount > 24):
            print("drink too much coke")

philip_cup = Coke(12)
philip_cup.fill()
philip_cup.refill(20)
print(f"Philip has {philip_cup.amount} of coke ")
