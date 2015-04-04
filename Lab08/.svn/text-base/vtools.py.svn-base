import re
import string

def is_valid_name(identifier):
    for letter in identifier:
        #print (letter)
        if(letter not in string.ascii_letters and letter not in string.digits):
            if(letter not in "_"):
                return False
    return True

def parse_pin_assignment(assignment):
    check = True
    port = ''
    if(assignment[0] not in "."):
        check =  False
    m = re.search(r'([\w_]+\()', assignment[1:])
    if(m):
        port = m.groups()[0][:-1]
        if(is_valid_name(port) is not True):
            check = False
    else:
        check = False
    pin = assignment[(2+len(port)):-1]
    #print(pin)
    if(is_valid_name(pin) is not True):
        check = False
    if(check is False):
        raise ValueError(assignment)
    
    return (port, pin)

def parse_net(line):
    #print(line)
    line = line.split()
    component = line[0]
    instance = line[1]
    if(is_valid_name(component) is False or is_valid_name(instance) is False):
        raise ValueError(line)
    ports = line[3:-1]
    ports[-1] = ports[-1]+','
    #print(ports)
    i = 0
    portpins = []
    #print(ports[0][1:-1])
    for port in ports:
        #if i == 0:
        #    portpin = parse_pin_assignment(port[1:-1])
        #    portpins.append(portpin)
        #    i = 1
        #else:
        portpin = parse_pin_assignment(port[:-1])
        #print(portpin)
        portpins.append(portpin)
    
    return (component, instance, tuple(portpins))



def main():
    #print(is_valid_name("hypphen"))
    #print("h" in string.ascii_letters)
    print(parse_pin_assignment('.Dasdf(n31232130)'))
    print(parse_net('DFFSR present_val_reg (.D(n30), .R(n33), .CLK(clk))'))
    

if __name__ == "__main__":
    main()