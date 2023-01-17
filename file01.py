def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s = []
    for i in data.split(","):
        s.append(int(i))
    return s
# Read data from file
path = "txt_file/data01.txt"
f = open(path).read()
print(main(f))