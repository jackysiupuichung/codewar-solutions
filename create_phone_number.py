def create_phone_number(n):
    str_list = [str(i) for i in n]
    str_list.insert(0, "(")
    str_list.insert(4, ") ")
    str_list.insert(8, "-")
    return "".join(str_list)
