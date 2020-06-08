def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    cache = {}

    for array in arrays:
        for elem in array:
            if elem not in cache:
                cache[elem] = 1
            else:
                cache[elem] += 1
    
    for val in cache:
        if cache[val] == len(arrays):
            result.append(val)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
