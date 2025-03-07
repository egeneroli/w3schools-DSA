
def merge_sort(values: list[int]) -> list[int]:
    # exit condition
    if len(values) <= 1:
        return values

    # recursion - merge the 2 arrays produced from recursing on 1st half and 2nd half
    # get midpoint index -- use int floor division to handle odd / even
    mid: int = len(values) // 2
    return merge(merge_sort(values[:mid]), merge_sort(values[mid:]))


def merge(lst1: list[int], lst2: list[int]) -> list[int]:
    lst: list[int] = []
    # while list 1 and 2 are not empty
    while lst1 and lst2:
        # if 1st list has lower first value, set as val and delete
        if lst1[0] < lst2[0]:
            val: int = lst1[0]
            del lst1[0]
        # if 2nd list has lower value, set to val and delete
        else:
            val: int = lst2[0]
            del lst2[0]
        # append value to result
        lst.append(val)

    # add any remaining elements from one list being longer -- empty list will add nothing
    lst.extend(lst1)
    lst.extend(lst2)

    return lst


print(merge_sort([7,6,4,9,2,8,6]))
