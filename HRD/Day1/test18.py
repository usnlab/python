#pos = ['Spot', 37.1413, 127.2034]
pos = ('Spot', 37.1413, 127.2034)

for i in range(len(pos)):
    print(pos[i], end=' ')

print()

for x,y in enumerate(pos):
    print(x, ' : ', y)