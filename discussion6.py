class Skittle:
    def __init__(self, color):
        self.color = color

class Bag:
    number_sold = 0
    
    def __init__(self):
        self.skittles = [] 
        Bag.number_sold += 1
    
    def tag_line(self):
        print("Taste the rainbow!")
    
    def print_bag(self):
        print([s.color for s in self.skittles])
        
    def take_skittle(self):
        return self.skittles.pop(0)
        
    def add_skittle(self, s):
        self.skittles.append(s)
        
    def take_color(self, color):
        for skittle in self.skittles:
            if skittle.color == color:
                return self.skittles.pop() # pops the current index
        return 'No skittle of that color in bag'
        
s1 = Bag()

# adding Skittle objects instances and instance attributes
for color in ['red', 'blue', 'yellow']:
    s1.add_skittle(Skittle(color)) 

ans = s1.take_color('yellow')
    
