import random
import time 

def naive_search(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(values) - 1

    if low > high:
        return -1

    midpoint = (low + high) // 2

    if values[midpoint] == target:
        return midpoint
    if target < values[midpoint]:
        return binary_search(values, target, low, midpoint - 1)
    return binary_search(values, target, midpoint + 1, high)


if __name__ == "__main__":
    # numbers = [1, 3, 5, 10, 12]
    # target = 10
    # print("Naive search index:", naive_search(numbers, target))
    # print("Binary search index:", binary_search(numbers, target))

    length = 10001
    sorted_list = set ()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")