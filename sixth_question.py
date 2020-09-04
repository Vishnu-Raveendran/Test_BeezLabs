hour, min = input().split(':')
minAngle = int(min)*6
hourAngle = int(hour)*30
print(str(abs(hourAngle - minAngle))+' degree')
