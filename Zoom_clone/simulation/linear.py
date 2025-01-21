import random,simpy

def LinearCongruenceMethod(X,m,a,c,random,noOfRandomNums):
     random[0]=X
     for i in range(1,noOfRandomNums):
          random[i]=((random[i-1]*a)+c)%m
LinearCongruenceMethod(10,7,3,4,random,8)