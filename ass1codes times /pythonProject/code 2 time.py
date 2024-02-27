import time


class Chocolate:
    def __init__(self, chocolate_id, weight, price, chocolate_type):
        self.id = chocolate_id
        self.weight = weight
        self.price = price
        self.type = chocolate_type


def merge_sort(chocolates, key='weight'):
    if len(chocolates) <= 1:
        return chocolates

    mid = len(chocolates) // 2
    left_half = chocolates[:mid]
    right_half = chocolates[mid:]

    left_half = merge_sort(left_half, key)
    right_half = merge_sort(right_half, key)

    sorted_chocolates = []
    while left_half and right_half:
        if key == 'weight':
            if left_half[0].weight < right_half[0].weight:
                sorted_chocolates.append(left_half.pop(0))
            else:
                sorted_chocolates.append(right_half.pop(0))
        elif key == 'price':
            if left_half[0].price < right_half[0].price:
                sorted_chocolates.append(left_half.pop(0))
            else:
                sorted_chocolates.append(right_half.pop(0))

    sorted_chocolates.extend(left_half)
    sorted_chocolates.extend(right_half)
    return sorted_chocolates


def test():
    chocolates = [Chocolate(1, 2, 5, "Dark"), Chocolate(6, 3, 15, "Caramel"), Chocolate(4, 2, 7, "Hazelnut")]

    start_time = time.time()
    sorted_by_weight = merge_sort(chocolates, 'weight')
    end_time = time.time()

    print("Chocolates sorted by weight:")
    for chocolate in sorted_by_weight:
        print("ID:", chocolate.id, "Weight:", chocolate.weight, "Price:", chocolate.price, "Type:", chocolate.type)
    print("Time taken to sort by weight:", end_time - start_time, "seconds")

    start_time = time.time()
    sorted_by_price = merge_sort(chocolates, 'price')
    end_time = time.time()

    print("\nChocolates sorted by price:")
    for chocolate in sorted_by_price:
        print("ID:", chocolate.id, "Weight:", chocolate.weight, "Price:", chocolate.price, "Type:", chocolate.type)
    print("Time taken to sort by price:", end_time - start_time, "seconds")


test()
