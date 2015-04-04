import re
import sys
import os.path

def main():
	if(len(sys.argv) != 2):
		return	
	filename = sys.argv[1]
	if(not os.path.isfile(filename)):
		return
	with open(filename ,'r') as f:
		lines = [x.strip('\n') for x in f.readlines()]
	for line in lines:
		m = re.match(r'def\s+(\w+)\(([\w=+,:\s]*)',line)
		if(m):
			print (m.groups()[0])
			args = re.split(',| ',m.groups()[1])
			i = 0
			for arg in args:
				if(arg):
					print('Arg' + str(i) + ': ' + arg)
					i+=1

if __name__ == "__main__":
    main()