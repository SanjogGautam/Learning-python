# Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck."
# It means Python cares about what an object can DO, not what its CLASS is.
#it is like dynamic typing
class Bird:
    def fly(self):
        print("Flying with feathers")

class Airplane:
    def fly(self):
        print("Flying with engines")

class Whale:
    def swim(self):
        print("Swimming in the ocean")

# This function uses Duck Typing
def let_it_fly(obj):
    # It doesn't check if obj is a Bird or Airplane. 
    # It just tries to call .fly()
    obj.fly()

# Testing the function
eagle = Bird()
boeing = Airplane()

let_it_fly(eagle)  # Works
let_it_fly(boeing) # Works
# let_it_fly(Whale()) # This would CRASH because a Whale can't .fly()
