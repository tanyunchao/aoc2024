
# part 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    target = 'XMAS'

    row = [[] for _ in range(len(lines))]
    for i, line in enumerate(lines):
        col = []
        for char in line:
            if char != '\n':
                col.append(char)
        row[i] = col
    
    def reverse_string(s):
        return s[::-1]

    for i in range(len(row)):
        for j in range(len(row[i])):

            #horizontal
            horiz = row[i][j:j+4]
            horiz = ''.join(horiz)
            if horiz == target:
                result += 1
            if reverse_string(horiz) == target:
                result += 1

            #vertical
            vertical = [row[i+k][j] for k in range(4) if i+k < len(row)]
            vertical = ''.join(vertical)
            if vertical == target:
                result += 1
            if reverse_string(vertical) == target:
                result += 1
                
            # positive diagonal
            pos_diag = [row[i+k][j+k] for k in range(4) if i+k < len(row) and j+k < len(row[i])]
            pos_diag = ''.join(pos_diag)
            if pos_diag == target:
                result += 1
            if reverse_string(pos_diag) == target:
                result += 1
            
            # negative diagonal
            neg_diag = [row[i+k][j-k] for k in range(4) if i+k < len(row) and j-k >= 0]
            neg_diag = ''.join(neg_diag)
            if neg_diag == target:
                result += 1
            if reverse_string(neg_diag) == target:
                result += 1

    print("🚀 part 1 result:", result)

# part 2
# 4 possible configurations of X-MAS only, can be rotated
# early terminate when middle isnt A
with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0

    row = [[] for _ in range(len(lines))]
    for i, line in enumerate(lines):
        col = []
        for char in line:
            if char != '\n':
                col.append(char)
        row[i] = col

    # extra 3x3 grid

    for i in range(len(row) - 2):
        for j in range(len(row[i]) - 2):
            grid = [[row[i+k][j+l] for l in range(3)] for k in range(3)]
            # early terminate if middle isnt A
            if grid[1][1] != 'A':
                continue
            
            # check all 4 possible configurations
            topLeft = grid[0][0]
            topRight = grid[0][2]
            bottomLeft = grid[2][0]
            bottomRight = grid[2][2]
            if topLeft == 'M' and topRight == 'M' and bottomLeft == 'S' and bottomRight == 'S':
                result += 1

            if topLeft == 'M' and bottomLeft == 'M' and topRight == 'S' and bottomRight == 'S':
                result += 1
            if topLeft == 'S' and bottomLeft == 'S' and topRight == 'M' and bottomRight == 'M':
                result += 1
            if topLeft == 'S' and topRight == 'S' and bottomLeft == 'M' and bottomRight == 'M':
                result += 1
        
    print("🚀 part 2 result:", result)


