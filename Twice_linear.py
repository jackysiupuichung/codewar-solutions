def dbl_linear(n):
    list = [1]
    y_pos = 0
    z_pos = 0
    while len(list) <= n:
        y = 2 * list[y_pos] + 1
        z = 3 * list[z_pos] + 1
        if y > z:
            list.append(z)
            z_pos += 1
        elif y < z:
            list.append(y)
            y_pos += 1
        elif y == z:
            list.append(y)
            z_pos += 1
            y_pos += 1
    print(list[n])
    return list[n]
