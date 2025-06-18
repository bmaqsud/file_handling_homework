def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    nums = data.split(',')
    nums = list(map(lambda num: int(num), nums))
    return nums

#  Read data from file
file_name = input("file name: ")
file_path = f"txt_file/{file_name}"
f = open(file_path)

data = f.read()
f.close()

lst = main(data)
print(lst)