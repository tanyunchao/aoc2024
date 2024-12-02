
# checks if valid based on increasing or decreasing, diff within correct bounds
def isValid(line):
    increasing = True
    if line[0] > line[1]:
        increasing = False
    valid = True

    for i in range(len(line) - 1):
        x = line[i]
        y = line[i + 1]
        if increasing:
            if x > y or abs(x - y) > 3 or abs(x - y) < 1:
                valid = False
                break;
        else:
            if x < y or abs(x - y) > 3 or abs(x - y) < 1:
                valid = False
                break;
    return valid

with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0

    for line in lines:
        line = line.split(" ")
        line = [int(x) for x in line]
        valid = isValid(line)
        if valid:
            result += 1
            continue;

    print("🚀 part 1 result:", result)



with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0

    for line in lines:
        line = line.split(" ")
        line = [int(x) for x in line]
        
        valid = isValid(line)

        if valid:
            result += 1
            continue;
            
        # remove one element at a time
        for i in range(len(line)):
            line2 = line.copy()
            line2.pop(i)
            valid = isValid(line2)
            if valid:
                result += 1
                break;

    print("🚀 part 2 result:", result)
    
