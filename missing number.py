'''Mahesh is given a box of Chocolates having unique numbers between 1 to N.
All chocolates are arranged in ascending order of their Number.
A friend has stolen one of th chocolates from the Box.
Given the array of size n-1, consisting of unique numbers from 1 to N (Max Value). Find the missing chocolate in the box
Input:
The first line of the test case is N - Denoting the Total Chocolates
The second line of the test case contains N-1 space separated numbers in array.
Output:
Print the missing chocolate in the box by calculating the missing number in array.'''
N=int(input())
arr=[]

while(N):
    arr=[int(x) for x in input().split()]
    if(arr.__len__()>N):
        arr.pop(x)
    break
sum = N* (N + 1) / 2
for i in y:
    sum = sum - int(i)
print(sum)