def merge_sort(array):
    if len(array) < 2:
        return array
    mid = int(len(array) / 2)

    # 左边
    lo = merge_sort(array[:mid])
    # 右边
    hi = merge_sort(array[mid:])

    merged_arr = []
    while lo and hi:
        merged_arr.append(lo.pop(0) if lo[0] <= hi[0] else hi.pop(0))

    merged_arr.extend(hi if hi else lo)

    return merged_arr


test_arr = [1, 2, 123, 10, 0, 300, 100]

print(merge_sort(test_arr))
