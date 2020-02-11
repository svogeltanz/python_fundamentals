'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Shoe:
    '''This is the superclass for shoes'''
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

    def __str__(self):
        return f"This is a {self.brand} shoe with size {self.size} which cost {self.price}€."

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





print("E x e c u t i o n    T i m e")
print("---------------------------")
print(" Shoe Class ")
print("---------------------------")

adi = Shoe("adidas", 44, 120)
print(adi)
ni = Shoe("nike", 43, 270)
combi = Shoe.__add__(adi, ni)
print(combi)
adi.expire()
print(adi)

print("---------------------------")
print(" University Class ")
print("---------------------------")

napier = University("Edinburgh Napier", 12000, "Scotland")
print(napier)
thm = University("Technische Hochschule Mittelhessen", 18000, "Germany")
print(thm)
thm.add_students(2500)
print(thm)

print("---------------------------")
print(" Adventure Class ")
print("---------------------------")

fuerte = Adventure("Spain", 650, 10)
egypt = Adventure("Egypt", 750, 14)
what = Adventure.__add__(fuerte, egypt)
print(what)
print(fuerte)
fuerte.last_minute(25)
print(fuerte)

