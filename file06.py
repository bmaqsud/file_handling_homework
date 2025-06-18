def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    rows=data.split('\n')
    length=[len(row) for row in rows]
    return length

with open('txt_file/data06.txt', 'r') as file :
    file_len=file.read()


result=main(file_len)
print(result)


    