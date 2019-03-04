from itertools import count

inp1=input().split()
N=int(inp1[0]) #no of elements
E=int(inp1[1])   #element to be found
count=0

while(N):
    inp2=[int(x) for x in input().split()]                          #converts a string list to int
    break
print(inp2)

if (inp2.count(E) not in inp2):         #if  E not present in inp2 print count as -1
    count= count-1
    print(count)
else:
    print(inp2.count(E))                    #else prints the no of occurrences of E in list



