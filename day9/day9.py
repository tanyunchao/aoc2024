def checksum(fileDecoded):
    result = 0
    for i in range(len(fileDecoded)):
        if fileDecoded[i] != '.':
            result += fileDecoded[i] * i 
    return result

# part 1
with open('input.txt', 'r') as file:
    result = 0
    line = file.readline()
    digits = [int(d) for d in str(line)]
    
    space = False
    count = 0
    fileDecoded = []
    for digit in digits:
        if not space:
            for i in range(digit):
                fileDecoded.append(count)
            space = not space 
            count += 1
        else:
            for i in range(digit):
                fileDecoded.append('.')
            space = not space
            
    left = 0 
    right = len(fileDecoded) - 1
    while fileDecoded[right] == '.':
        right -= 1
    
    while left < right:
        if fileDecoded[left] == '.':
            temp = fileDecoded[right]
            fileDecoded[right] = fileDecoded[left]
            fileDecoded[left] = temp
            right -= 1
            while fileDecoded[right] == '.':
                right -= 1
            left += 1
        else:
            left += 1
    
    print(checksum(fileDecoded))
            
    print(result)
    
# part 2

with open('input.txt', 'r') as file:
    result = 0
    line = file.readline()
    digits = [int(d) for d in str(line)]
    # spaces are [size of space, index of start of space]
    spaces = []
    
    space = False
    count = 0
    fileDecoded = []
    for digit in digits:
        if not space:
            for i in range(digit):
                fileDecoded.append(count)
            space = not space 
            count += 1
        else:
            for i in range(digit):
                fileDecoded.append('.')
            spaces.append([digit, len(fileDecoded) - digit])
            space = not space
            
    # print("len(spaces): ", len(spaces))
    # print("len(fileDecoded): ", len(fileDecoded))
    # print("starting spaces: ", spaces)
    # print("starting file: ", fileDecoded)

    right = len(fileDecoded) - 1
    prev_digit = 10000000
    # print(fileDecoded)
    # start rightward and check for size of files to be moved 
    while len(spaces) > 0 and right > 0:
        # print(spaces)
        # seek leftward to find "tail" of the rightmost file 
        while fileDecoded[right] == '.':
            right -= 1    
        
        # out of bounds
        if right < 0:
            break;
                
        # check size of file
        left = right 
        size = 0
        while fileDecoded[left] == fileDecoded[right]:
            left -= 1
            size += 1
        
        # if number has been shifted before, skip
        if fileDecoded[right] > prev_digit:
            right = left 
            continue
        
        # print("digit in play: ", fileDecoded[right])
        
        # add back to left to act as head of file 
        left += 1        

        prev_digit = fileDecoded[right]
        # check for spaces w size >= size of file
        for space in spaces:
            # can only shift leftward if, if space starting index is greater than left index
            # means that its gonna shift right == gg
            # no point checking further also as the future spaces are more rightward as well
            # applys for all cases
            if space[1] >= left:
                print("illegal shift, broken out")
                break;
            
            # move file to space
            if space[0] == size:
                space_head = space[1]
                for i in range(size):
                    fileDecoded[space_head] = fileDecoded[left]
                    fileDecoded[left] = '.'
                    space_head += 1
                    left += 1
                spaces.remove(space)
                break;
            # move file to space but update the space size and index
            elif space[0] > size:
                space_head = space[1]
                for i in range(size):
                    fileDecoded[space_head] = fileDecoded[left]
                    fileDecoded[left] = '.'
                    space_head += 1
                    left += 1
                space[0] -= size
                space[1] += size
                if space[0] <= 0:
                    print("space removed: ", space)
                    spaces.remove(space)
                if space[1] < 0:
                    print("space removed: ", space)
                    spaces.remove(space)
                break;
                
                
        
        # last step: move rightward by size of file
        right -= size
    # print(spaces)
    # print(len(fileDecoded))
    # print(fileDecoded)
    
    print(''.join(str(d) for d in fileDecoded))
    
    
    print(checksum(fileDecoded))
