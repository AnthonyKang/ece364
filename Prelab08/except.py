a = input("Please enter some values:").split()
total = 0
for value in a:
	try:
		total = total + float(value)
	except:
		pass
	finally:
		pass
print('The sum is:',total)