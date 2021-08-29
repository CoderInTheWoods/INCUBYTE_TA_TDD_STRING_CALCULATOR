def add(numbers):
    if numbers == "": return 0
    elif numbers.startswith("//"):numbers = numbers.replace(numbers[2],',')[4:]
    else:numbers = numbers.replace('\n',',')
    
    numbers = list(map(int, numbers.split(',')))

    negative_nums = list(filter(lambda x: x < 0, numbers))
    if negative_nums:
        raise Exception(str('negatives not allowed : '),str(negative_nums))

    return sum(numbers)