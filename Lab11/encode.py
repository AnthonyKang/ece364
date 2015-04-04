a = 199 ^ 1 if (1 if 199 & 128 else 0) else 199
#print(1 if 199 & 128 else 0)
#print(a)

message = 98
medium = [199, 182, 180, 189, 200, 218, 225, 215]
n = 0
for i in medium:
    n = 7 if n is 0 else n - 1
    #print(message & 2)
    #print(2**n)
    #i = (2**n & message)
    #i = i ^ 1 if (0 if (2**n & message) & (i & 1) else 1) else i
    i = i | 1 if message & 2**n else i & 254 
    print(i)
   
    print(n)

message = 9

a = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6 ]
print(a)
b = []
for i in range(6):
    b = b + a[i::6]
print(b)

a=[]
for i in range(5):
    a = a + b[i::5]
print(a)