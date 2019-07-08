class Person(object):
    species = 'Human'
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat() # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __repr__(self):
        return f'{self.name} is a person'
    
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.previous = []

    def say(self, stuff):
        self.previous += [stuff]
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        if self.previous:
            return str(self.previous[-1])
        return 'I said nothing'
        
    def start_again(self):
        full = ' '.join([self.previous[i] for i in range(len(self.previous))])
        return full
