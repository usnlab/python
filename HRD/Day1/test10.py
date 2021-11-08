kor=0; eng=0; hap=0; avg=0; mesg=''; 

#kor = input('KOR : ')
kor = int(input('KOR : '))
eng = int(input('ENG : '))
print()

#hap = kor + eng <<< String 으로 처리 
#hap = int(kor) + int(eng)
hap = kor + eng
avg = hap / 2 

print('HAP = ', hap)
print('AVG = ', avg)
if avg >= 70 : 
    mesg = 'Succeeded'
else : 
    mesg = 'Failed'

print('Result : ', mesg)

