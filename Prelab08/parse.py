import sys

try:
	f = open(sys.argv[1])
	lines = f.readlines()
	rows = []
	for line in lines:
		rows.append(line.split())
	for row in rows:
		total = 0
		count = 0
		string = ''
		for num in row:
			try:
				total = total + int(num)
				count += 1
			except ValueError:
				if(len(string) > 2):
					string = string + ' ' + num
				else:
					string = string + num
		if(total):
			print('{0:.3f}'.format(total/count), string)
		else:
			print(string)
except IndexError:
	print("Usage: Pparse.py [filename];")
except IOError as e:
	print(sys.argv[1], "is not a readable file.")
else:
	pass
finally:
	pass