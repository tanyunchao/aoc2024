with open('input.txt', 'r') as file:
    lines = file.readlines()
    first = []
    second = []
    for line in lines:
        line = line.strip()

        split = line.split("   ")
        first.append(int(split[0]))
        second.append(int(split[1]))

# part 1
    first.sort()
    second.sort()

    print(first)
    print(second)

    result = 0
    for i in range(len(first)):
        result += abs(first[i] - second[i])

    print("🚀 part 1 result:", result)
    
# part 2
with open('input.txt', 'r') as file:
    lines = file.readlines()
    first = []
    second = {}
    for line in lines:
        line = line.strip()

        split = line.split("   ")
        first.append(int(split[0]))
        if int(split[1]) not in second:
            second[int(split[1])] = 1
        else:
            second[int(split[1])] += 1
    print(second)
        
    result = 0 
    for i in range(len(first)):
        if first[i] in second:
            result += second[first[i]] * first[i]

    print("🚀 part 2 result:", result)

