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

# write a class for shoes (running)
# use __init__ to set the constructor
# use __str__ to print info about the class
# learn about the __add__ method
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

# write a class for clothes
class Clothes:
    '''Class for clothes'''

    def __init__(self, type, season, age_in_months):
        self.type = type
        self.season = season
        self.age_in_months = age_in_months

    def __str__(self):
        return f"Type: {self.type}, Season: {self.season}, Age in months: {self.age_in_months}"

    def __add__(self, other):
        total_type = f"{self.type}, {other.type}"
        total_season = f"{self.season}, + {other.season}"
        total_age_in_months = f"{self.age_in_months}, {other.age_in_months}"
        return Clothes(total_type, total_season, total_age_in_months)


# write a class for food
class Food:
    '''Class for food'''

    def __init__(self, type, season, bio):
        self.type = type
        self.season = season
        self.bio = bio

    def __str__(self):
        return f"Type: {self.type}, Season: {self.season}, Bio: {self.age_in_months}"

    def __add__(self, other):
        total_type = f"{self.type}, {other.type}"
        total_season = f"{self.season}, + {other.season}"
        total_age_in_months = f"{self.age_in_months}, {other.age_in_months}"
        return Clothes(total_type, total_season, total_age_in_months)

shoe1 = Shoe("Asics", 75, "Sports")
shoe2 = Shoe("Adidas", 50, "Everday life")
print(shoe1)
print(shoe2)