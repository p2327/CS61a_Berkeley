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


class Pet(object):
    
    def __init__(self, name, owner):
        self.is_alive = True # why pass it into the init and not class?
        self.name = name
        self.owner = owner
        
    def __repr__(self):
        return f"{self.name} is {self.owner}'s pet"
    
    def eat(self, thing):
        print(f'{self.name} ate a {thing}!')
        
    def talk(self):
        print('Woof!')
        
#####################
#####################

class Cat(Pet):
    
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
        
    def talk(self):
        print('Meow')
        
    def lose_life(self, num):
        self.lives -= num
        if self.lives <= 0:
            self.is_alive = False
            print(f'{self.name} lost all his lives')
        return self.lives
            
    def _1up(self):
        self.lives += 1
        self.is_alive = True
        return self.lives

"""mr_waffles = Pet('Mr Waffles', 'Nicol')

print(mr_waffles)

mr_waffles.eat('cookie')

mr_waffles.talk()"""

tor = Cat('Thor', 'Jona')


tor.talk()

test = tor.is_alive

tor.lose_life(9)

tor._1up()

test = tor.is_alive
