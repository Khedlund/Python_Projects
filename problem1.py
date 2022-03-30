# @author Katharine Hedlund

def isect(str1, str2):
    # Finds the unique integers the appear in both str lists and contain the digit 2.
    # Parameters: Takes two str, each representing a comma-separated sequence of integers.
    # Returns: the result as a sorted list of int.

    str1 = str1.split(",")
    str2 = str2.split(",")
    result = []

    for num in str1:
        if ('2' in num) and (num in str2):
            print(num)
            result.append(int(num))

    # eliminate duplicates and sort
    result = list(set(result))
    result.sort()

    return result

