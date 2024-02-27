 # Creating a chocolate class with the attributes
class Chocolate:
    def __init__(self, chocolate_id, weight, price, chocolate_type):
        self.id = chocolate_id
        self.weight = weight
        self.price = price
        self.type = chocolate_type

#Creating the student class
class Student:
    def __init__(self, name, chocolate=None):#Initializing a student with a name and an assigned chocolate
        self.name = name
        self.chocolate = chocolate

# Define the find_chocolate function
def find_chocolate(students, attribute, value): #Looking for a chocolate from a student with the specified attribute
    for student in students: #For every student in students
        if student.chocolate: #For the assigned chocolate to that student
            if attribute == 'price' and student.chocolate.price == value: #Check if the attribute we are looking for is price with the specific value
                return student #Return that student
            elif attribute == 'weight' and student.chocolate.weight == value: #Else if we are looking for specified calue for weight with the specified value
                return student #Retthn that student
    return None #Else return none of the students of none of them have the specified weigt or price of that specific value

# Test Case:
# Define a list of Student objects named 'students'
students = [
    Student("Rawdha"),
    Student("Salama", chocolate=Chocolate(1, 5, 10, "Peanutbutter Chocolate")),
    Student("Mahra", chocolate=Chocolate(2, 7, 15, "Milk")),
    Student("Ahmed", chocolate=Chocolate(3, 2, 8, "Almond"))
]

# Search for a chocolate with price 10
results = find_chocolate(students, 'price', 10)
if results:
    print("The student with the chocolate of a price of 10 is", results.name)
else:
    print("No student holds a chocolate with price 10.")

# Search for a chocolate with a weight of 10
results = find_chocolate(students, 'weight', 2)
if results:
    print("The student with the chocolate of a weight of 8 grams is", results.name)
else:
    print("No student holds a chocolate with weight 8 grams.")
