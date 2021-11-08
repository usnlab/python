# Python Practice

num1,num2,hap,mok=(0,0,0,0)
#num1=90; num2=85
try:
    #pass
    num1 = int(input('1st num : '))
    num2 = int(input('2nd num : '))
    hap = num1 + num2
    mok = num1 / num2
except Exception as ex:
    print('Error Occurrd :', ex)

print(f'{num1}+{num2}={hap}')
print(f'{num1}/{num2}={round(mok,2)}')
print()

x = [7,25.2,'abc',34]
for data in x:
    try:
        y=data**2
        print(y, end=' ')
    except:
        print()
        
