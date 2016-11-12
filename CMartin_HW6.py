#With this assignment, we'll take a look at some of what the numpy module can do.  
#Do both of the following:

#Part 1
#Using your submission of homework 1 as a base, replace as many of the functions as you can with numpy functions.
#For example, instead of using your sort function that you wrote, use numpy.sort.
#Refer to here for most of the functions you'll need.

import numpy as np
import copy

setup = '''
import numpy as np
import copy

#Sort Functions:
def sortwithloops(input):
    """loops through the set and sorts"""
    input2 = []
    for i in sorted(input):
        input2.append(i)
    return input2

def sortwithoutloops(input): 
    """Sort a list without loops"""
    return sorted(input)

def sortwithnumpy(input):
    return np.sort(input)

#Search Functions:

def searchwithloops(input, value):
    """loops through the set and extracts the desired value"""
    input2 = []
    for item in input:
        if item == value:
            input2.append("True")
        else:
            input2.append("False")
    return "True" in input2

def searchwithoutloops(input, value):
    """extracts a desired value using a built in list function """
    return value in input #return a value	

def searchwithnumpy(input, value):
    output = np.where(input == value)
    if np.size(output) > 0:
        result = "True"
    else:
        result = "False"
    return result

np.random.seed(123)
l100 = np.random.randint(1, 1000, size=100)
L100 = l100.tolist()
l1000 = np.random.randint(1, 1000, size=1000)
L1000 = l1000.tolist()
l10000 = np.random.randint(1, 1000, size=10000)
L10000 = l1000.tolist()

a100 = np.random.randint(1, 1000, size=100)
A100 = np.array(a100)
a1000 = np.random.randint(1, 1000, size=1000)
A1000 = np.array(a1000)
a10000 = np.random.randint(1, 1000, size=10000)
A10000 = np.array(a10000)
'''

#Part 2
#Using the timeit function measure the execution times of all the sort and search functions you have.
#You'll most likely need to do a large number of tests on each one to get a meaningful result.
#Something like 10,000 or more.   
#Your submission will be a single file that has all the functions from homework 1 and the additional approach using numpy.
#Additionally, you will have the timing of all the functions output to the console. Something like.
#    Sort using iteration:  x loops = y seconds
#    Sort using built in python: x' loops = y' seconds
#    Sort using numpy: x'' loops  = y''seconds 

#NOTE: APOLOGIZES FOR THE CONFUSING NUMBERING SYSTEM, I ADDED MORE TEST CASES AFTER AND DID NOT CHANGE THE NAMING CONVENTIONS

import timeit
n = 1000
t_sort1 = timeit.timeit("x=copy.copy(L100); sortwithloops(x)", setup=setup, number=n)
t_sort2 = timeit.timeit("x=copy.copy(L100); sortwithoutloops(x)", setup=setup, number=n)
t_sort3 = timeit.timeit("x=copy.copy(L100); sortwithnumpy(x)", setup=setup, number=n)

n1 = 1000
t2_sort1 = timeit.timeit("x=copy.copy(L1000); sortwithloops(x)", setup=setup, number=n1)
t2_sort2 = timeit.timeit("x=copy.copy(L1000); sortwithoutloops(x)", setup=setup, number=n1)
t2_sort3 = timeit.timeit("x=copy.copy(L1000); sortwithnumpy(x)", setup=setup, number=n1)

n2 = 10000
t3_sort1 = timeit.timeit("x=copy.copy(L100); sortwithloops(x)", setup=setup, number=n2)
t3_sort2 = timeit.timeit("x=copy.copy(L100); sortwithoutloops(x)", setup=setup, number=n2)
t3_sort3 = timeit.timeit("x=copy.copy(L100); sortwithnumpy(x)", setup=setup, number=n2)

n3 = 10000
t4_sort1 = timeit.timeit("x=copy.copy(L1000); sortwithloops(x)", setup=setup, number=n3)
t4_sort2 = timeit.timeit("x=copy.copy(L1000); sortwithoutloops(x)", setup=setup, number=n3)
t4_sort3 = timeit.timeit("x=copy.copy(L1000); sortwithnumpy(x)", setup=setup, number=n3)

n4 = 1000
t5_sort1 = timeit.timeit("x=copy.copy(L10000); sortwithloops(x)", setup=setup, number=n4)
t5_sort2 = timeit.timeit("x=copy.copy(L10000); sortwithoutloops(x)", setup=setup, number=n4)
t5_sort3 = timeit.timeit("x=copy.copy(L10000); sortwithnumpy(x)", setup=setup, number=n4)

n5 = 10000
t6_sort1 = timeit.timeit("x=copy.copy(L10000); sortwithloops(x)", setup=setup, number=n5)
t6_sort2 = timeit.timeit("x=copy.copy(L10000); sortwithoutloops(x)", setup=setup, number=n5)
t6_sort3 = timeit.timeit("x=copy.copy(L10000); sortwithnumpy(x)", setup=setup, number=n5)

print '''
Functions repeated 1000 times with 100 items   1000 items   10000 items
Sort With Loops                 :   %.4f sec   %.4f sec     %.4f sec  
Sort Without Loops (base Python):   %.4f sec   %.4f sec     %.4f sec
Sort With NumPy                 :   %.4f sec   %.4f sec     %.4f sec
----------------------------------------------------------------------------
Functions repeated 10000 times with 100 items  1000 items   10000 items
Sort With Loops                 :   %.4f sec   %.4f sec     %.4f sec
Sort Without Loops (base Python):   %.4f sec   %.4f sec     %.4f sec
Sort With NumPy                 :   %.4f sec   %.4f sec     %.4f sec
''' %(t_sort1, t2_sort1, t5_sort1, t_sort2, t2_sort2, t5_sort2, t_sort3, t2_sort3, t5_sort3, t3_sort1, t4_sort1, t6_sort1, t3_sort2, t4_sort2, t6_sort2, t3_sort3, t4_sort3, t6_sort3)

#n = 1000
t_search1 = timeit.timeit("x=copy.copy(A100); searchwithloops(x, 988)", setup=setup, number=n)
t_search2 = timeit.timeit("x=copy.copy(A100); searchwithoutloops(x, 988)", setup=setup, number=n)
t_search3 = timeit.timeit("x=copy.copy(A100); searchwithnumpy(x, 988)", setup=setup, number=n)

#n1 = 1000
t2_search1 = timeit.timeit("x=copy.copy(A100); searchwithloops(x, 988)", setup=setup, number=n1)
t2_search2 = timeit.timeit("x=copy.copy(A100); searchwithoutloops(x, 988)", setup=setup, number=n1)
t2_search3 = timeit.timeit("x=copy.copy(A100); searchwithnumpy(x, 988)", setup=setup, number=n1)

#n2 = 10000
t3_search1 = timeit.timeit("x=copy.copy(A1000); searchwithloops(x, 988)", setup=setup, number=n2)
t3_search2 = timeit.timeit("x=copy.copy(A1000); searchwithoutloops(x, 988)", setup=setup, number=n2)
t3_search3 = timeit.timeit("x=copy.copy(A1000); searchwithnumpy(x, 988)", setup=setup, number=n2)

#n3 = 10000
t4_search1 = timeit.timeit("x=copy.copy(A1000); searchwithloops(x, 988)", setup=setup, number=n3)
t4_search2 = timeit.timeit("x=copy.copy(A1000); searchwithoutloops(x, 988)", setup=setup, number=n3)
t4_search3 = timeit.timeit("x=copy.copy(A1000); searchwithnumpy(x, 988)", setup=setup, number=n3)

#n4 = 1000
t5_search1 = timeit.timeit("x=copy.copy(A10000); searchwithloops(x, 988)", setup=setup, number=n4)
t5_search2 = timeit.timeit("x=copy.copy(A10000); searchwithoutloops(x, 988)", setup=setup, number=n4)
t5_search3 = timeit.timeit("x=copy.copy(A10000); searchwithnumpy(x, 988)", setup=setup, number=n4)

#n5 = 10000
t6_search1 = timeit.timeit("x=copy.copy(A10000); searchwithloops(x, 988)", setup=setup, number=n5)
t6_search2 = timeit.timeit("x=copy.copy(A10000); searchwithoutloops(x, 988)", setup=setup, number=n5)
t6_search3 = timeit.timeit("x=copy.copy(A10000); searchwithnumpy(x, 988)", setup=setup, number=n5)

print '''
Functions repeated 1000 times with 100 items     1000 items     10000 items
Search With Loops                 :   %.4f sec   %.4f sec       %.4f sec
Search Without Loops (base Python):   %.4f sec   %.4f sec       %.4f sec
Search With NumPy                 :   %.4f sec   %.4f sec       %.4f sec
----------------------------------------------------------------------------
Functions repeated 10000 times with 100 items    1000 items     10000 items
Search With Loops                 :   %.4f sec   %.4f sec       %.4f sec
Search Without Loops (base Python):   %.4f sec   %.4f sec       %.4f sec
Search With NumPy                 :   %.4f sec   %.4f sec       %.4f sec
''' %(t_search1, t2_search1, t5_search1, t_search2, t2_search2, t5_search2, t_search3, t2_search3, t5_search3, t3_search1, t4_search1, t6_search1, t3_search2, t4_search2, t6_search2, t3_search3, t4_search3, t6_search3)
