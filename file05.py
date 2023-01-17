def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    number = 0

    for i in data:
        number+=i.isdigit()


    return [number,len(data)-number]
# Read data from file
path = "txt_file/data05.txt"
f = open(path).read()
print(main(f))