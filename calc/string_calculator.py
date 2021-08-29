def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace('\n',',')
    return sum(map(int, numbers.split(',')))