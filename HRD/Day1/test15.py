#test.py

a=19;b=0;tot=0;div=0
try:
    tot=a+b
    div=a/b
except Exception as ex:
    #pass
    print('Error :', ex)

print('TOT : ', f'{a}+{b}={tot}')
print('DIV : ', f'{a}/{b}={round(div,3)}')