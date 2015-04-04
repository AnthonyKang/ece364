from lists import *

first_list = list(map(int,input("Enter the first list of numbers: ").split()))
second_list = list(map(int,input("Enter the second list of numbers: ").split()))
[Median, Sorted_List] = find_median(first_list,second_list)
print('First list:', first_list)
print('Second list:', second_list)
print('Merged list:', Sorted_List)
print('Median', Median)