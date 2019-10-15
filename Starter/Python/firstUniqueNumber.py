# Fast O(n) solution using a dictionary
# Python: first unique number in a list
def solution(lst):
    counts = {}

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in lst:
        if counts[item] == 1:
            return item

    return -1

print(solution([1,2,1,3,2,5])) # prints 3
print(solution([1,2,1,3,3,2,5])) # prints 5
print(solution([1,2,1,3,3,2,5,5])) # prints -1
print(solution([7])) # prints 7
