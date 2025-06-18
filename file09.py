def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
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
    return min(nums)

with open('txt_file/data09.txt', 'r') as file:
     min_num=file.read()

result=main(min_num)
print(result)
