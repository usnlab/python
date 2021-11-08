import json

### Save : dumps() / Open : loads()

user = {
    'id' : 100, 
    'name' : 'HKD', 
    'age' : 34
}

svdata = json.dumps(user, ensure_ascii=False)
print('Sava Success')
opdata = json.loads(svdata)
print('Read : ', opdata)

for i,j in opdata.items():
    print (i, "-", j)

for key in opdata:
    print (key, "=", opdata[key])