class Link:
        """A linked list with a first element and the rest."""
        empty = ()
        def __init__(self, first, rest=empty):
            assert rest is Link.empty or isinstance(rest, Link)
            self.first = first
            self.rest = rest
        def __getitem__(self, i):
            if i == 0:
                return self.first
            else:
                return self.rest[i-1]
        def __len__(self):
            return 1 + len(self.rest)
            

# s = Link(3, Link(4))

# len(s)

# a = s[1]

# b = s[0]


def link_expression(s):
        """Return a string that would evaluate to s."""
        if s.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + link_expression(s.rest)
        return f'Link({s.first}{rest})'

# ans = link_expression(s)

# adding repr method as link_expression to class Link
Link.__repr__ = link_expression

# s

# s_first = Link(s, Link(4))

# len(s_first)

x = Link(3, Link(1))

len(x)
