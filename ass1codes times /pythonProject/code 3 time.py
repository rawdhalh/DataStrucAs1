import time

class Chocolate:
    def __init__(self, chocolate_id, weight, price, chocolate_type):
        self.id = chocolate_id
        self.weight = weight
        self.price = price
        self.type = chocolate_type

class Student:
    def __init__(self, name, chocolate=None):
        self.name = name
        self.chocolate = chocolate

def find_chocolate(students, attribute, value):
    start_time = time.time()
    for student in students:
        if student.chocolate:
            if attribute == 'price' and student.chocolate.price == value:
                end_time = time.time()
                print("Time taken to find chocolate by price:", end_time - start_time, "seconds")
                return student
            elif attribute == 'weight' and student.chocolate.weight == value:
                end_time = time.time()
                print("Time taken to find chocolate by weight:", end_time - start_time, "seconds")
                return student
    end_time = time.time()
    print("Time taken to find chocolate:", end_time - start_time, "seconds")
    return None

# Test Case:
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
