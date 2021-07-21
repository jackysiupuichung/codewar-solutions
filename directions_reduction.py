def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    path = [] #initialize stack
    for dir in arr:
        #if path not empty and previous direction is opp of current direction
        if path != [] and dict[dir] == path[-1]:
            path.pop()
        else:
            path.append(dir)
    return path
