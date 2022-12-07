#< >
season = ""
month = int(input("Input the month (1 - 12) or (January - December): "))

if month in ('December', 'January', 'February', 12, 1, 2):
	season = 'winter'
if month in ('September', 'October', 'November', 9, 10, 11):
	season = 'autumn'
if month in ('June', 'July', 'August', 6, 7, 8):
	season = 'summer'
if month in ('March', 'April', 'May', 3, 4, 5):
	season = 'spring'	

print("Season is",season)	