class Number:
    
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)
        
    def __coerce__(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
            
    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other.type_tag)]
        return coercion_fn(self)
        
    coercions = {('rat', 'com') = rational_to_complex}
