'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Shoe:

    '''Class for shoes'''

    def __init__(self, model, price, purpose):
        self.model = model
        self.price = price
        self.purpose = purpose

    def __str__(self):
        return f"Model: {self.model}, Price: {self.price}, Purpose: {self.purpose}"

    def __add__(self, other):
        total_model = f"{self.model}, {other.model}"
        total_cost = self.price + other.price
        total_purpose = f"{self.purpose}, {other.purpose}"
        return Shoe(total_model, total_cost, total_purpose)



class SportShoe(Shoe):

    def __init__(self, model, price, purpose, miles_ran):
        super().__init__(model, price, purpose="sports")
        self.miles_ran = miles_ran

    def __str__(self):
        return super().__str__() + f", Actual miles ran: {self.miles_ran}"

    def increaseMiles(self):
        last_run = int(input("How long has your last run been?"))
        self.miles_ran += last_run
        return self.miles_ran


asics = SportShoe("GT1000", 75, 0, 350)
print(asics)
