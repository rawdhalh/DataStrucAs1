import time
start_time = time.time()
class Chocolate:
    def __init__(self, chocolate_id, weight, price, chocolate_type):
        """ class to represent the chocolate"""
        self.id = chocolate_id
        self.weight = weight
        self.price = price
        self.type = chocolate_type


class Student:
    def __init__(self, name):
        """ class to represent the student"""

        self.name = name
        self.chocolate = None  # set the student to have no chooclates


def distribute_chocolates_iterative(chocolates, students):
    if len(chocolates) < len(students):  # check if the lengths of the chocolates is less than the amount of students
        print(
            "Error: Not enough chocolates to distribute to all students.")  # if there are more students than chocolates we print this statement
        return  # if not, we continue

    assigned_chocolates = set()  # Create a to keep track of assigned chocolate IDs to make sure we dont repeat the chocolates
    for student in students:  # for loop to check for every student in the students
        if chocolates:
            chocolate = chocolates.pop(0)  # Take the first chocolate from the list
            student.chocolate = chocolate  # Assign the current chocolate to the student
            if chocolate.id in assigned_chocolates:  # check if the chocolate ID is in the assigned chocolate list (check if another student already has it)
                print("Error: Two students got the same chocolate.")  # print an error message
                return
            assigned_chocolates.add(chocolate.id)  # Add the chocolate ID to the set of assigned chocolates
        else:
            print("Error: Not enough chocolates to distribute to all students.")
            return


def recusive_distribution(chocolates, students, index=0, assigned_chocolates=set()):
    # Recursively distribute the differnt chocolates to the students

    # Creating a base case for the recursion: If there are no more chocolates or students, stop the recursion
    if index >= len(chocolates) or index >= len(students):
        return

    student = students[index]
    chocolate = chocolates[index]

    # Check if the chocolate ID has already been assigned to another student.
    if chocolate.id in assigned_chocolates:
        print("Error: Two students got the same chocolate.")
        return

    # Assign the chocolate to the current student.
    student.chocolate = chocolate
    assigned_chocolates.add(chocolate.id)

    # the index is incremented by 1 to move to the next chocolate and the next student.
    recusive_distribution(chocolates, students, index + 1, assigned_chocolates)


# Test Cases
def test():
    chocolates = [Chocolate(2, 5, 2, "Almond"), Chocolate(5, 7, 4, "Peanut butter Chocolate"),
                  Chocolate(3, 4, 3, "White")]
    students = [Student("Rawdha"), Student("Salama"), Student("Maitha")]

    print("Iterative Distribution:")
    distribute_chocolates_iterative(chocolates[:], students[:])
    for student in students:
        if student.chocolate:
            print(student.name, "has selected chocolate ID", student.chocolate.id, "type", student.chocolate.type)
        else:
            print(student.name, "did not get any chocolate.")

    print("\nRecursive Distribution:")
    chocolates = [Chocolate(2, 5, 2, "Almond"), Chocolate(5, 7, 4, "Peanut butter Chocolate"),
                  Chocolate(3, 4, 3, "White")]
    students = [Student("Rawdha"), Student("Salama"), Student("Maitha")]
    recusive_distribution(chocolates, students)
    for student in students:
        if student.chocolate:
            print(student.name, "has selected chocolate ID", student.chocolate.id, "type", student.chocolate.type)
        else:
            print(student.name, "did not get any chocolate.")


test()
end_time = time.time()
elapsed_time = end_time - start_time

print(elapsed_time)