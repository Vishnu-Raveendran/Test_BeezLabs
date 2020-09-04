number = input().strip()
while len(number) != 1:
    cnt = 0
    for item in number:
        cnt+=int(item)
    number = str(cnt)
print(number)
