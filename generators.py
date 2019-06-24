def letters_generator():
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current)+1)

""" for letter in letters_generator():
    print(letter) """
    
letters_a_d = letters_generator()
    
next(letters_a_d)


def letters_maker(start, finish):
    while start <= finish:
        yield start
        start = chr(ord(start) + 1)
        
alphabet = letters_maker('a', 'z')

# returns the next letter in the alphabet (range of letters..)
next(alphabet)


""" The first time next is called, the program executes statements from the body of the letters_maker
function until it encounters the yield statement. Then, it pauses and returns the value of start.
Yield statements do not destroy the newly created environment; they preserve it for later. 
When next is called again, execution resumes where it left off. The values of start and of 
any other bound names in the scope of letters_maker are preserved across subsequent calls to next."""

# print all the letters between assigned values of start and finish
for letter in alphabet:
    print(letter)
    
 
