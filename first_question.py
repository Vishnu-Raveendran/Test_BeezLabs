Strng = 'Beezlabs is a startup to be a part of microsoft start-up program'
print(Strng)
count = 0
for items in Strng:
    item = ord(items)
    if (item >= 65 and item <= 90) or (item >= 97 and item <= 122):
        count+=1
print('Number of Characters:' + str(count))
