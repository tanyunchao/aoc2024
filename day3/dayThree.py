import re
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#     result = 0

#     for line in lines:
#         pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
#         doPattern = r"do\()"
#         dontPattern = r"don't\()"
#         # Use re.findall to find all matches
#         matches = re.findall(pattern, line)

#         for match in matches:
#             result += int(match[0]) * int(match[1])
            
        

        

#     print("🚀 part 1 result:", result)
    
# part 2
with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0

    enabled = True  # Start enabled by default
    for line in lines:
        
        # Find all patterns (mul, do, don't) in order of appearance
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
        for match in re.finditer(pattern, line):
            match_text = match.group()
            print(match_text)
            
            if match_text == "do()":
                enabled = True
            elif match_text == "don't()":
                enabled = False
            else:  # mul(x,y)
                if enabled:
                    num1, num2 = map(int, match.groups())
                    result += num1 * num2

    print("🚀 part 2 result:", result)
