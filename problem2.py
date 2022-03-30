# Q: you don't have to declare a variable until you use it in python?
# Q: do the tabs actually change the code in python? incorrect tabbing, incorrect code?
# @author Katharine Hedlund

def expand(rng):
# Expands ranges in a list of integers. Ranges formatted "a-b" in the list are expanded as [a,b), which is left-inclusive/right-non-inclusive.
# Parameters: str, representing a comma separated list of integers or integer ranges.
# Returns: a sorted list of int with the specified integers and expanded integer ranges and no duplicates.

    rng = rng.split(",")
    result = []

    for num in rng:
        if "-" in num:
            dashIndex = num.index('-')
            start = int(num[:dashIndex])
            stop = int(num[dashIndex + 1:])

            # generate the range of numbers to add
            numList = list(range(start, stop))

            # add range to result, check for duplicates
            for digit in numList:
                if digit not in result:
                    result.append(digit)
        else:
            if int(num) not in result:
                result.append(int(num))

    result.sort()
    return result








