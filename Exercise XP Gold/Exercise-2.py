month = input("Input the month (1 - 12) or (January - December): ")

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March'):
	season = 'spring'
elif (month == 'June'):
	season = 'summer'
elif (month == 'September'):
	season = 'autumn'
elif (month == 'December'):
	season = 'winter'

print("Season is",season)