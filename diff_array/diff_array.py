def array_diff(a, b):
    return a if not b else [x for x in a if x != b[0]]
