#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:09:05 2022

@author: lesliecook
"""
import math

#create empty list and initialize variables
xlist = []

    #accept list size from user
n = int(input("Enter the sample size: "))
    #run loop till size of list using for loop and range() function
for i in range(0, n):
            print("Enter a number: ")
        #use input() function to get numbers from user
            x = float(input())
        #add number to the list using append() function
            xlist.append(x)
            print('\n')

print('The user list is: ', xlist)
print('\n')

list_sum = 0
for x in xlist:
        list_sum +=x

def SampleMean():
    for x in xlist:
        list_mean = list_sum / n
        return list_mean

def SampleVar():
        list_sq = 0
        for x in xlist:
                list_sq += x**2
                list_var = list_sq / (n-1)
                return list_var

def SampleSD():
        for x in xlist:
                list_sd = math.sqrt(SampleVar)
                return  list_sd

def display():

        print(' i \t\t\t Xi \t\t(Xi-Xbar) \t\t\t (Xi-Xbar)^2')
        print('______________________________________________')

        print('______________________________________________')
        print('SUM: {value:2.3f}'.format(value= list_sum))
        print('The sample size is: ', n)
        print('The mean of the sample set is: {value:2.3f}'.format(value = SampleMean()))
        print('The variance of the sample set is: {value:2.3f}'.format(value = SampleVar()))
        print('The standard deviation of the sample set is: {value:2.3f}'.format(value = list_sd)


def main():
    display()

main()
