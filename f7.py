def add(a,b):
	sum = a+b
	return sum

def mul(a,b):
	mul = a*b
	return mul

x = int(input('Enter a number : '))  #10
y = int(input('Enter a number : '))  #20

ans1 = add(x,y)               #10 + 20 =30
ans2 = mul(x,y)               #10 * 20 =200
ans = ans1+ans2                 # 30 + 200 = 230
print(ans)