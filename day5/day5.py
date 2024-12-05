import functools
from functools import cmp_to_key

def get_middle(arr):
    # Get length of array
    length = len(arr)
    
    # If array is empty, return None or raise exception
    if length == 0:
        return None
    
    # For odd length arrays, return the middle number
    if length % 2 == 1:
        return arr[length // 2]
    
    # For even length arrays, return average of two middle numbers
    # If you want both middle numbers, return them as a tuple
    middle_right = length // 2
    middle_left = middle_right - 1
    return (arr[middle_left] + arr[middle_right]) / 2
    # OR return (arr[middle_left], arr[middle_right])
        
# part 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    flag = True
    pagesOrder = {}
    books = []

    for line in lines:
        line = line.strip()

        if line == '':
            flag = False
            continue
        if flag:
            line = line.split('|')
            a = int(line[0])
            b = int(line[1])            
            if a not in pagesOrder:
                pagesOrder[a] = set()
            pagesOrder[a].add(b)
        else:
            line = line.split(',')
            line = [int(i) for i in line]
            books.append(line)
    
    wrongOrder = []           
    for book in books:
        works = True
        # loop through every single number, make sure number on the left is legit
        for i in range(len(book) - 1):
            # j is the number on the right
            for j in range(i + 1, len(book)):
                if book[j] not in pagesOrder[book[i]]:
                    works = False
                    break
        if works:
            print("🚀🚀🚀")
            result += get_middle(book)
        else: 
            wrongOrder.append(book)
    print("part 1 result", result)
    
    part2 = 0
    for book in wrongOrder:
        def custom_compare(a_list, b_list):
            def count_valid_relationships(lst, book):
                count = 0
                pageOrder = pagesOrder[lst]
                for i in book:
                    if i in pageOrder:
                        count += 1

                return count
            
            # Get counts for both lists
            a_count = count_valid_relationships(a_list, book)
            b_count = count_valid_relationships(b_list, book)
            print(a_count, b_count)
            
            # If counts are different, sort by count
            if a_count != b_count:
                return b_count - a_count  # Higher count comes first
            
            # If counts are equal, check if elements of one list exist in pagesOrder of the other
            # Check if any number in a_list exists in pagesOrder[b] for any b in b_list
            a_pageOrder = pagesOrder[a_list]
            b_pageOrder = pagesOrder[b_list]
            
            if b in a_pageOrder:
                return 1
            if a in b_pageOrder:
                return -1
            
            print("🚀🚀🚀fdajfn a")
            return 0  # Lists are equivalent for sorting purposes

        sortedBook = sorted(book, key=cmp_to_key(custom_compare))
        part2 += get_middle(sortedBook)
        
    print("part 2 result", part2)