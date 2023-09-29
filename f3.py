#simple interest with function........

def simple_interest(amount,rate,year):
	ans = (amount*rate*year) / 100
	print('simple interest =',ans)

amount = int(input('Enter amount : '))
rate = int(input('Enter rate : '))
year = int(input('Enter year : '))

simple_interest(amount,rate,year)
