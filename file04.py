def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    chars=[]
    for w in data:
        if w not in '0123456789':
           chars.append(w)
    return chars


with open('txt_file/data04.txt', 'r') as file:
    string=file.read()

result=main(string)
print(result)