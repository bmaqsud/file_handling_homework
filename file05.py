def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    w_total=0
    n_total=0
    for i in data:
        if i in '0123456789':
            n_total += 1
        else:
            w_total += 1
    return w_total, n_total


with open('txt_file/data05.txt', 'r') as file :
    w_n_total=file.read()

result=main(w_n_total)
print(result)