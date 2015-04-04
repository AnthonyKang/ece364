import re

def main():
	FILEOUT = open( 'Part2.out', 'wt' )
	with open('Part2.in' ,'r') as f:
		lines = [x.strip('\n') for x in f.readlines()]
	for line in lines:
		line = re.sub(r'(purdue.edu)',r'ecn.\1',line)
		line = re.sub(r'(\d$)',r'\1/100',line)
		line = str(line)
		print(line)
		FILEOUT.write(line)



if __name__ == "__main__":
    main()