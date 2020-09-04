inpt = list(map(int, input().split()))
start, end = min(inpt), max(inpt)
result = ''
for item in range(start, end+1):
    if item not in inpt:
        result += str(item)
print('The missing number from ' + str(start) + ' to ' + str(end) + ' is ' + result)
