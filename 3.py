Name:M.harshani
Date:16/05/2019

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
  Suppose the following input is supplied to the program:
  8
  Then, the output should be:
  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
  
  
Description:
The  given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Step1:Start
Step2:Declare variable n
Step3:Declare dictionary d=dict()
Step4:for i in range(1,n+1):
    d[i]=i*i
Step5:Display dict


Program:
n=int(input("enter the number"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)


OUTPUT:
enter the number8
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}