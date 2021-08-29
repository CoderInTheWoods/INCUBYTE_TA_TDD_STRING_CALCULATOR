def add(numbers):
    if numbers == "":
        return 0
    elif numbers.startswith("//"):
        numbers = numbers.replace(numbers[2],',')[4:]
    else:
        numbers = numbers.replace('\n',',')
    return sum(map(int, numbers.split(',')))