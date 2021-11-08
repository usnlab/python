
y = 0; sum = 0 
while True :
    y = y + 1
    sum = sum + y
    print (y, end=' ')
    
    if y == 5:
        continue
    elif y == 10:
        break
    else:
        continue    

print()
print('Total : ', sum)