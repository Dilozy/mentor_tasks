def my_zip(iterable1, iterable2):
    shortest_len = min(len(iterable1), len(iterable2))
    return ((iterable1[i], iterable2[i]) for i in range(shortest_len))
