def smallest_number(value):
    numbers = value.split()
    if not all(part.isdigit() and 0 <= int(part) <= 9 for part in numbers):
        return "Invalid"
    if not all(part.isdigit() for part in value.split()):
        return "Invalid"
    if len(numbers) > 10:
        return "Invalid"
    if len(numbers) < 2:
        return "Invalid"
    
    numbers.sort()
    if numbers[0] == "0":
        for i in range(1, len(numbers)):
            if numbers[i] != "0":
            
                numbers[0], numbers[i] = numbers[i], "0"
                break

    result = ''.join(numbers)

    return result
output = input()
print(smallest_number(output))
