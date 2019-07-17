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
        
    def take_all(self):
        for skittle in self.skittles:
            print(skittle.color)
        self.skittles = ()
        
s1 = Bag()

# adding Skittle objects instances and instance attributes
for color in ['red', 'blue', 'yellow']:
    s1.add_skittle(Skittle(color)) 

ans = s1.take_all()
    
    


"""
    def take_all(self):
        out = [s for s in self.skittles]
        for s in self.skittles:
            self.skittles.remove(s)
        del self.skittles[0]
        print([s.color for s in out])
        return out
        """
