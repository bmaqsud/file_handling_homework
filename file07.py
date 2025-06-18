def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
# Read data from file
     
    total=0
    for i in data:
        if i in '123456789':
            total += int(i)

    return total


with open('txt_file/data07.txt', 'r') as file :
    data_sum=file.read()

result=main(data_sum)
print(result)