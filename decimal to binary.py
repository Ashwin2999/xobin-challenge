'''Given a number N, Write a program that generates and prints the value of all binary numbers from 1 to N.
Input:The test case contains an Integer N.
Output: Print all binary numbers with from 1 to n . The output for the testcase must be in a single line and space separated.
Note:The Binary digits are separated by space. But ensure that there are no trailing or preceeding spaces while printing the output.'''
def binary(n):
    arr = [0] * n  # array to store binary number
    i=0                         #setting count to 0
    while(n>0):           #while input is not equal to 0 or greater than 0
        arr[i]=n%2            #storing the remainder in array
        n = int(n/2 )      #quotient becomes the inp
        i=i+1                           #incrementing the index of array by 1 each time the element is added into the array

    #for loop to print array in reverse order
    for j in range(i-1,-1,-1):                  #for(j=i-1;j>=-1;j--)
        print(arr[j],end="")
    return " "

if __name__=='__main__':
    n=inp = int(input())  # input decimal number
    for x in range (1,n+1):
        print(binary(x),end=" ")
