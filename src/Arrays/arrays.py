
def min_val(values: list[int]) -> int:
    """

    :param values:  list of ints
    :return: minumum value
    """
    min_value: int = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value

print(min_val([2,3,5,8]))