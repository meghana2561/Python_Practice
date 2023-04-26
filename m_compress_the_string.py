import itertools
s = input()
for i,k in itertools.groupby(s):
    print('(%d, %d)'%(len(list(k)),int(i)),end = " ") 
