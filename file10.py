def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    rows=data.split('\n')
    lenth=[len(row) for row in rows]
    return lenth

with open('txt_file/data10.txt', 'r') as file:
    max_lenth=file.read()

result=main(max_lenth)
print(result)
print(max(result))