#!/usr/bin/python3

def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """ 
    with open(filename,'w') as file:
        return file.write(text)

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)   