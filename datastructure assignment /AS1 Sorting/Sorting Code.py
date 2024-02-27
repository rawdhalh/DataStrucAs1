class Chocolate:
    def __init__(self, chocolate_id, weight, price, chocolate_type):
        self.id = chocolate_id
        self.weight = weight
        self.price = price
        self.type = chocolate_type


def merge_sort(chocolates, key='weight'):
    # Merge sort implementation to sort chocolates by weight by stating that the key= wieght
    if len(chocolates) <= 1:  # Checking if there are enough chocolates
        return chocolates

    # Split the list into two halves
    mid = len(chocolates) // 2
    left_half = chocolates[
                :mid]  # left_half contains elements from the beginning of chocolates up to and exluding the midpoint

    right_half = chocolates[mid:]  # right_half contains the elements from the midpoint to the end

    # Recursively sort each half with the key (in this case it is the weight of the chocolates)
    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    # Merge the two already sorted halves
    sorted_chocolates = []  # Creating an empty list for the sorted chocolates
    while left_half and right_half:
        # If we are sorting by weight, then
        if key == 'weight':
            if left_half[0].weight < right_half[
                0].weight:  # check if the chocolate in the left hand side is smaller than the right hand side
                sorted_chocolates.append(left_half.pop(
                    0))  # if it is, then we append it to the sorted_chocolates list and remove it from left_half
            else:  # if the chocolate in the right hand side is smaller than the right hand side
                sorted_chocolates.append(
                    right_half.pop(0))  # Append it to the sorted_chocolates list and remove it from the right_half
        elif key == 'price':  # Repeating the same process, but with price as our parameter that we are checking
            if left_half[0].price < right_half[0].price:
                sorted_chocolates.append(left_half.pop(0))
            else:
                sorted_chocolates.append(right_half.pop(0))

    # Add the remaining elements from both of the halves
    sorted_chocolates.extend(left_half)
    sorted_chocolates.extend(right_half)

    return sorted_chocolates


# Test Cases
def test():
    # Creating a list of chocolates including their attributes (ID, weight, price, and type)
    chocolates = [Chocolate(1, 2, 5, "Dark"), Chocolate(6, 3, 15, "Caramel"), Chocolate(4, 2, 7, "Hazelnut")]

    # Sort chocolates by weight
    sorted_by_weight = merge_sort(chocolates, 'weight')
    print("Chocolates sorted by weight:")
    for chocolate in sorted_by_weight:
        print("ID:", chocolate.id, "Weight:", chocolate.weight, "Price:", chocolate.price, "Type:", chocolate.type)

    # Sort chocolates by price
    sorted_by_price = merge_sort(chocolates, 'price')
    print("\nChocolates sorted by price:")
    for chocolate in sorted_by_price:
        print("ID:", chocolate.id, "Weight:", chocolate.weight, "Price:", chocolate.price, "Type:", chocolate.type)


test()  # calling the test case function to run
