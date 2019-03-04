'''Problem Statement
Bharat is given a string that contains text and numbers.
 Bharat needs to extract the number from the string such that the number must not contain the integer 9.
NOTE: In case there any multiple numbers that match the condition, Print all numbers in a space separated format( in same order that they appear in the
string)
For eg if the string contains "My pin code is 560047 and phone number is 98998" , Bharth only needs to extract 560047 and not 98998.
You need to help him extract the number.
Input:
The testcase consists of a String S
Output:
Output the extracted number.'''
S=input().split()
for i in S:
                                                                                                                                    #S.find(x) finds x if x is present in string S
    if(S.isdigit()==True and S.find('9')!=0 ) :                                                #S.isdigit() returns bool value (true) if the input string contains only integer
        print(i,end=" ")



