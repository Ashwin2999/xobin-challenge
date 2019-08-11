#a=first num; b=common diff; n=length of series
#a+(a+b)+(a+2b)+.........
#tn=a+(n-1)b is the nth term
#sum of n terms= (n/2)[2a+(n-1)b]
#b=Tn-(Tn-1)

inp = input().split()
A=int(inp[0])           #first num
B=int(inp[1])           #step size or diff
N=int(inp[2])           #size of series
for i in range(N):
   # tot=int( (N/2)*[2*A+((N-1)*B)] )
    sub1= (N/2) * (2*A + ((N-1)*B))
    #sub2= 2*A +((N-1)*B)
    #tot=sub1*sub2
print(int(sub1))
