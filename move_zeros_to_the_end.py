def move_zeros(array):
    zeros = []
    list = []
    for chr in array:
        if chr == 0 or 0.0:
            if type(chr) == float or type(chr) == int:
                zeros.append(chr)
            else:
                list.append(chr)
        else:
            list.append(chr)
    return list + zeros
