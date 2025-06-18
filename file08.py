def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    nums=[]
    for i in data:
        if i in '0123456789':
            nums.append(int(i))
    return max(nums)
        
with open('txt_file/data08.txt', 'r') as file:
    max_nums=file.read()

result=main(max_nums)
print(result)