# a=7; b=2; hap=0; cha=0; gob=0; mok=0 
a,b,hap,cha,gob,mok = (7,2,0,0,0,0)

print('test03.py 2:05')

hap = a + b
cha = a - b 
gob = a * b
mok = a / b

print('+ : ', hap)
# print('- : ', cha)
# print('* : ', gob)
# print('/ : ', mok)
print('-' * 15)
print(a, ' + ', b, ' = ', hap)

print('%d+%d=%d' %(a,b,hap))
print('{}+{}={}'.format(a,b,hap))
print(f'{a}+{b}={hap}')