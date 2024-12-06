# # part 1
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
    
#     layout = []
#     for line in lines:
#         layout.append(list(line.strip()))
    
#     UP = '^'
#     DOWN = 'v'
#     LEFT = '<'
#     RIGHT = '>'
#     OBSTACLE = '#'
#     TRAVERSED = 'X'
#     guard = UP
    
#     x = 0
#     y = 0
#     for line in layout:
#         x = 0
#         for char in line:
#             if char == guard:
#                 print(x, y)
#                 break;
#             x += 1
#         if char == guard:
#             break;
#         y += 1


#     while x < len(layout[0]) and x >= 0 and y < len(layout) and y >= 0:
#         print(x, y)
#         # hit obstacle reverse motion and rotate
#         if layout[y][x] == OBSTACLE:
#             if guard == UP:
#                 y += 1
#                 guard = RIGHT
#             elif guard == DOWN:
#                 y -= 1
#                 guard = LEFT
#             elif guard == LEFT:
#                 x += 1
#                 guard = UP
#             elif guard == RIGHT:
#                 x -= 1
#                 guard = DOWN
            
#             # continue bc we hit obstacle and we dont want to traverse it
#             continue;
        
#         layout[y][x] = TRAVERSED
        
#         # move forward
#         if guard == UP:
#             y -= 1
#         elif guard == DOWN:
#             y += 1
#         elif guard == LEFT:
#             x -= 1
#         elif guard == RIGHT:
#             x += 1

#     # layout[y][x] = TRAVERSED
    
#     # Write layout to file
#     with open('layout.txt', 'w') as output_file:
#         for row in layout:
#             output_file.write(''.join(row) + '\n')
        
#     result = 0
#     for line in layout:
#         for char in line:
#             if char == TRAVERSED:
#                 result += 1

#     print(result)

# part 1
import copy


with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    layout = []
    for line in lines:
        layout.append(list(line.strip()))

    # length and width of layout == 130
    length = len(layout)
    width = len(layout[0])
    
    originalObstacleCount = 0    
    for i in range(length):
        for j in range(len(layout[0])):
            if layout[i][j] == '#':
                originalObstacleCount += 1

    availableSpaces = length * width - originalObstacleCount

    def get_solution(map, availableSpaces):
        UP = '^'
        DOWN = 'v'
        LEFT = '<'
        RIGHT = '>'
        OBSTACLE = '#'
        TRAVERSED = 'X'
        guard = UP
        
        x = 0
        y = 0
        for line in map:
            x = 0
            for char in line:
                if char == guard:
                    break;
                x += 1
            if char == guard:
                break;
            y += 1


        while x < len(map[0]) and x >= 0 and y < len(map) and y >= 0 and availableSpaces > 0:
            # hit obstacle reverse motion and rotate
            if map[y][x] == OBSTACLE:
                if guard == UP:
                    y += 1
                    guard = RIGHT
                elif guard == DOWN:
                    y -= 1
                    guard = LEFT
                elif guard == LEFT:
                    x += 1
                    guard = UP
                elif guard == RIGHT:
                    x -= 1
                    guard = DOWN
                
                # continue bc we hit obstacle and we dont want to traverse it
                continue;
            
            map[y][x] = TRAVERSED
            availableSpaces -= 1
            
            # move forward
            if guard == UP:
                y -= 1
            elif guard == DOWN:
                y += 1
            elif guard == LEFT:
                x -= 1
            elif guard == RIGHT:
                x += 1


        if availableSpaces == 0:
            return False
        
        return True
    
    result = 0
    counter = 0

    for i in range(length):
        for j in range(width):
            counter += 1
            print(counter)
            if layout[i][j] == '#':
                continue
            layoutCopy = copy.deepcopy(layout)
            
            layoutCopy[i][j] = '#'
            if not get_solution(layoutCopy, availableSpaces):
                result += 1

    print("🚀 part 2 result", result)