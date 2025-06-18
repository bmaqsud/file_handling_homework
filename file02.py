def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    

#  Read data from file
     
    return len(data)


with open('txt_file/data02.txt', 'r') as file:
    file_data=file.read()

result=main(file_data)
print(result)