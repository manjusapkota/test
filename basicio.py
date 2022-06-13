# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:22:11 2022

@author: manju sapkota

"""
#io-input/output
#output
print("hello")
var1=456
print(var1)
print(13==34)
#print("hello"+var1)#error
print("hello"+str(var1))
print("hello{}".format(var1))

num=4**0.5
print(num)
num1=25**0.5

print(num1)
#input
var1=input("enter any value:")
print("hello"+str(var1))
print("hello{}".format(var1))
#read and display single number
var8=input("enter a number:")
a=int(var8)
print(a)
#read and  display two integer number
#declare
#input
#process
#type conversion str->int
#add two number

#output
num1 = None
num2 =None
num3=None
tmp=None
num1=input("Enter first no:")
#num1=int(num1)
num1=float(num1)
num2=input("enter a second no:")
#num2=int(num2)
num2=float(num2)
tmp=str(123)#int->str
tmp=str(123.456)#float->str
num3=num1+num2


print("first no{}".format(num1))
print("second no:{}".format(num2))
print("sum :{}".format(num3))

var4=input("enter any valie:")
print("hello"+str(var1))
