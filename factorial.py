'''An Integer I is called a factorial number if it is the factorial of a positive integer.
The First few Factorial Numbers are 1,2,6,24
(0! =1 1!=1 2! =2   3!= 6).
Given a number I, Write a Program that prints all factorial numbers less than or equal to I.'''

def factorial(n):               #function that performs factorial
    fact=1                              #initially assigning the factorial value to 1
    for i in range (1,n+1):       #for(i=1;i<=inp,i++). sinc
        fact=fact*i
    return fact                         #returns the factorial

if __name__=='__main__':            #main function
    inp = int(input())  # takes the input
    for j in range(1,inp+1):                #displays numbers from range 1,inp+1 based of inp
        #print(factorial(j) , end=" ")                               #obj j calling factorial fuction
        while(factorial(j) < inp):
             print(factorial(j) , end=" ")
             break