""" saves content of the file to a list """
def save_file_to_list(filename):
    """
    saves a file to a list
    input: filename
    return: list
    """
    lines = []
    with open(filename, 'r') as f:
        for i in f:
            lines.append(i)
    return lines



def get_len_of_list(lista):
    """
    returns the length of the list
    input:list
    output: number
    """
    return len(lista)
