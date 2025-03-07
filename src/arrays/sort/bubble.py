
def bubble_sort(values: list[int]) -> list[int]:

    # iterate n times
    for i in range(len(values)-1):

        # create boolean variable for tracking if swap occurred this iteration
        swapped: bool = False

        # iterate through array
        for i in range(len(values)-1):
            # check value and next
            # if not ascending, swap
            if values[i] > values[i+1]:
                temp: int = values[i]
                values[i] = values[i+1]
                values[i+1] = temp
                swapped = True

        # break out if no swaps occurred this iteration
        if not swapped:
            break

    return values


print(bubble_sort([9,5,7,23,87,84,36]))