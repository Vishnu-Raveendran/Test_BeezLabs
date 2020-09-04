start_range = int(input('Start range: '))
end_range = int(input('End range: '))
counter = 0
for item in range(start_range, end_range+1):
    counter += str(item).count('1')
print(counter)
