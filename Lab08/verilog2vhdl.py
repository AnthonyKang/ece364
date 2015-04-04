import sys
from vtools import *

if(len(sys.argv) > 3):
    print("Usage: verilog2vhdl.py [infile] [outfile]")
    sys.exit(1)

if(len(sys.argv) >= 2):
    try:
        input_file = open(sys.argv[1], 'r')
    except IOError as e:
        print (e)
        sys.exit(2)

if(len(sys.argv) == 3):
    try:
        output_file = open(sys.argv[2], 'a')
    except IOError as e:
        print (e)
        sys.exit(3)
else:
    output_file = sys.stdout

if(len(sys.argv) < 2):
    sys.exit(0)

lines = input_file.readlines()
vhdl_lines = []
for line in lines:
    vhdl_lines.append(parse_net(line))

out_string = ''
for line in vhdl_lines:
    #print (line)
    if(is_valid_name(line[0]) is False or is_valid_name(line[1]) is False):
        print('Error: input file is not a valid Verilog port map!')
        sys.exit(4)
    out_string = line[0] + ': ' + line[1] + ' PORT MAP('
    for i in range(len(line)-1):
        #print (i)
        out_string = out_string + str(line[2][i][0]) + '=>' + str(line[2][i][1]) + ', '
    out_string = out_string + str(line[2][-1][0]) + '=>' + str(line[2][-1][1]) + ');\n'
    output_file.write(out_string)

sys.exit(0)