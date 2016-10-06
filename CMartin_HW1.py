#Your first homework assignment will be a quick and easy jump into Python. 
#For this and next week's assignments, I will supply a basic template that you need to expand upon.
#Attached is a file hw1_template.py.  

#Do all of the following:
#    Download and install Python 2.7.x on your computer.
#    Fill in the 4 functions in hw1_template.py.
#I want to be able to run the main function and see correct values printed from the function calls. 

#The functions are:
#    sortwithloops.  Take the input list and return a sorted list, do not use list functions.
#Do this just looping through the values.  Use any kind of sort you wish.
#    sortwithoutloops: Take the input list and return a sorted list, use list functions.
#    searchwithloops: Takes two inputs, the list and a value to search for.
#Returns true if the value is in the list, otherwise false.  Do not use list functions.
#Do this just looping through, with any kind of search.
#    searchwithoutloops: Takes two inputs, the list and a value to search for. 
#Returns true if the value is in the list, otherwise false.  Use list functions. 

#Submit by attaching the completed .py file to your submission.  I will run "python hw1.py" (or whatever you call it) to see if your solution is correct. 

#This and the next assignment should be pretty easy.  This helps me do a quick assessment on the class before we move forward. 
#If you have a lot of trouble with these assignments, please let me know.


#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):
    """loops through the set and sorts"""
    for f in sorted(input):
        print f
    return #return a value
	
#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input): 
    """Sort a list without loops"""
    input.sort
    print input
    return #return a value

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):
    """loops through the set and extracts the desired value"""
    for item in input:
        if item == value:
            print True
        else:
            print False
    return #return a value

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):
    """extracts a desired value using a built in list function """
    print value in input
    return #return a value	

if __name__ == "__main__":	
    L = [5,3,6,3,13,5,6]	

    print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    print searchwithloops(L, 5) #true
	print searchwithloops(L, 11) #false
    print searchwithoutloops(L, 5) #true
	print searchwithoutloops(L, 11) #false


