def pig_it(text):
    new = " "
    text_list = text.split(" ")
    for i in text_list:
        if i in '!.%&?':
            new += i
        else:
            new += i[1:] + i[0] + "ay" + " "
    return new.strip(" ") #remove space
