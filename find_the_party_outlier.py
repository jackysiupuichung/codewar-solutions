def find_outlier(integers):
    list = [int % 2 for int in integers]
    if list.count(0) == 1:
        return integers[list.index(0)]
    else:
        return integers[list.index(1)]
