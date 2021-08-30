no_of_calls = 0
def add(numbers):

    global no_of_calls
    no_of_calls += 1

    if numbers == "": return 0
    elif numbers.startswith("//"):
        if not '[' in numbers:
            numbers = numbers.replace(numbers[2],',')[4:]
        else:
            delimiter_info, num_str = numbers.split('\n')
            final_delimiter_list = [x[:-1] for x in delimiter_info[2:].split('[')[1:]]
            for x in final_delimiter_list: num_str = num_str.replace(x,',')
            numbers = num_str

    else:numbers = numbers.replace('\n',',')
    
    numbers = list(map(int, numbers.split(',')))
    numbers = list(filter(lambda x: x <= 1000, numbers))

    negative_nums = list(filter(lambda x: x < 0, numbers))
    if negative_nums:
        raise Exception(str('negatives not allowed : '),str(negative_nums))

    return sum(numbers)

def GetCalledCount():
    global no_of_calls
    return no_of_calls