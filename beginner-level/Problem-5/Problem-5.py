Input = [1, [2, 3], [4, [5]]]
B = []
def flatten_list(A):
    for item in A:
        if isinstance(item, list):
            B.extend(flatten_list(item))
        else:
            B.append(item)
    return B


print(flatten_list(Input))