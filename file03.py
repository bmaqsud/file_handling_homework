def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    nums=[]
    for i in data:
         if i in '0123456789':
             nums.append(int(i))
    return nums


with open('txt_file/data03.txt', 'r') as file:
     file_data=file.read()

result=main(file_data)
print(result)

