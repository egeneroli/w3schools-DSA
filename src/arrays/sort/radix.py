
def radix_sort(vals: list[int]) -> list[int]:
    print(vals)
    # sort by buckets / digits

    # get max digits
    max_len: int = len(str(max(vals)))

    for i in range(1, max_len+1):

        # create buckets
        buckets: list[list[int]] = [[] for _ in range(10)]

        # iterate through values, place in buckets
        for val in vals:
            # get last digit
            s: str = str(val).zfill(max_len)[-i]
            d: int = int(s)

            # place in bucket
            buckets[d].append(val)

        # print(buckets)
        vals = [x for bucket in buckets for x in bucket]
        # print(vals)

    return vals


print(radix_sort([2,71,33,84,25]))
