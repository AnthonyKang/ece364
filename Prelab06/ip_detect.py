import re

def main():
	with open('addys.in' ,'r') as f:
		lines = [x.strip('\n') for x in f.readlines()]
	for line in lines:
		m = re.match(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}:([0-9]{1,4}|[12][0-9]{4}|3[01][0-9]{3}|32[0-6][0-9]{2}|327[0-5][0-9]|3276[0-7])',line) 
		if(m):
			if(int(m.groups()[3]) < 1024):
				print(m.group() + ' - Valid (root privileges required)')
			else:
				print(m.group() + ' - Valid')
		else:
			print(line + ' - Invalid IP Address')


if __name__ == "__main__":
    main()