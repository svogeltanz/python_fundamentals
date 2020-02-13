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
    '''This is the superclass for shoes'''
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

    def __str__(self):
        return f"This is a {self.brand} {self.__class__.__name__} with size {self.size} which cost {self.price}€."

    def __repr__(self):
        return f"{self.brand} in {self.size} for {self.price}."

    def __add__(self, other):
        brand = f"{self.brand}, {other.brand}"
        size = (self.size + other.size)/2
        price = self.price + other.price
        return Shoe(brand, size, price)

    def __len__(self):
        return f"The length of the shoe is size {self.size}."

    def expire(self):
        print(f"This {self.brand} cannot be used anymore.")
        self.brand = "expired " + self.brand


class Running(Shoe):
    '''This is a sub class for running shoes'''

    def __init__(self, brand, size, price, use_case, km_ran):
        super().__init__(brand, size, price)
        self.use_case = use_case
        self.km_ran = km_ran

    def __str__(self):
        return f"This is a {self.brand} {self.__class__.__name__} Shoe with size {self.size} which cost {self.price}€. " \
            f"It has {800-self.km_ran} km until it expires and is especially for {self.use_case} running."

    def add_exercise(self, num):
        self.km_ran += num
        print(f"You just added {num} to total km.")
        if self.km_ran > 800:
            print("You might think about some new shoes.")

            def __str__(self):
                print("This shoe should not be used anymore.")

class Track(Running):

    def __str__(self):
        return f"Those are running shoes especially for {self.__class__.__name__}."

    def add_exercise(self, num):
        self.km_ran += num
        print(f"You just ran {self.km_ran} with this shoe, nice!")
        if self.km_ran > 400:
            print(f"Shoes for {self.__class__.__name__} are sensitive. You have to replace them.")

            def __str__ (self):
                print(f"Those shoes are too old.")



class University:

    def __init__(self, name, students, country):
        self.name = name
        self.students = students
        self.country = country

    def __str__(self):
        return f"This is the {self.name} {self.__class__.__name__} with {self.students} students based in {self.country}."

    def __repr__(self):
        return f"{self.brand} {self.__class__.__name__} in {self.country} with {self.students} students."

    def __len__(self):
        return {self.students}

    def add_students(self, new_students):
        self.students = (self.students + new_students)
        return self.students



class Adventure:

    def __init__(self, country, price, length):
        self.country = country
        self.price = price
        self.length = length

    def __str__(self):
        return f"This is a trip to {self.country} with a length of {self.length} which costs {self.price}."

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.country} for {self.price}€ and {self.length} days."

    def __len__(self):
        return f"{self.length} days."

    def __add__(self, other):
        country = f"{self.country} {other.country}"
        price = self.price + other.price
        length = self.length + other.length
        return Adventure(country, price, length)

    def last_minute(self, deduction):
        print(f"This {self.__class__.__name__} just got cheaper!")
        self.price = (self.price*(100-deduction)/100)
        return self.price



print("----------Running Shoe-------------------")
adi = Running("Adidas", 45, 160, "track", 0)
print(adi)
adi.add_exercise(15)
print(adi)
print("----------Running Shoe for Track-------------------")
sauc = Track("Saucony", 45, 220, "Track", 395)
print(sauc)
sauc.add_exercise(10)
print(sauc)