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
            numbers = num_str.replace(delimiter_info[3:-1],',')

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