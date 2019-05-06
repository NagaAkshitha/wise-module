rem=0
result=0
num =2**1000


while num>0:
	rem=num%10
	result=result+rem
	num=num/10
print result
