
def quick_sort(values: list[int]) -> list[int]:
    # exit condition
    # if array is one element, it is already sorted
    if len(values) <= 1:
        return values

    # recursion
    # choose pivot index / value
    # p: int = len(values) // 2
    pivot: int = values[0]

    # order so values to left of pivot are lower and values to right are higher
    left: list[int] = [x for x in values if x < pivot]
    right: list[int] = [x for x in values if x > pivot]
    middle: list[int] = [pivot for _ in range(len(values)-len(left)-len(right))]

    # recursively sort sub arrays
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([1,5,7,3,9,3,2,8]))

