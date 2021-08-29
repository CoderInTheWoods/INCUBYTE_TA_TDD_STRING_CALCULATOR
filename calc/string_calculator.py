def add(numbers):
    if numbers == "":
        return 0
    elif len(numbers.split(',')) == 1:
        return int(numbers)
    elif len(numbers.split(',')) == 2:
        return sum(map(int, numbers.split(',')))