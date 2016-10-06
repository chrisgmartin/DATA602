#Write a software program
#Your code needs to be able to handle exceptions.
#It should handle all data as specified by the data definition document from Lesson 2
#and throw some kind of error when it encounters data that doesn't match that format.
#To test this, I will add the line 'vlow, vlow, 1, 1, vbig, vhigh' to the .csv file.
#Your program should gracefully handle this line in all cases from the previous part. 

#1. Loads in the data from cars.data.csv.

#use Tkinter to import the csv file
import Tkinter, tkFileDialog
root = Tkinter.Tk()
root.withdraw()
fileimport = tkFileDialog.askopenfilename(parent = root)

#use pandas to read the csv file and create a dataframe
import pandas as pd
try:
    cardata = pd.read_csv(fileimport, names=['buying', 'maint', 'doors', 'persons', 'lub_boot', 'safety', 'class'], na_values=['NA'])
    print "File read \nImported as table: cardata"
except:
    print "Read error, try again"

#2. In the main portion of your program you should run the following operations and print the result to the console (except d).
#a. Print to the console the top 10 rows of the data sorted by 'safety' in descending order
#add new column for variable  safety rating
cardata['safetyrate'] = cardata['safety'].replace("vhigh",1)
cardata['safetyrate'] = cardata['safetyrate'].replace("high",2)
cardata['safetyrate'] = cardata['safetyrate'].replace("med",3)
cardata['safetyrate'] = cardata['safetyrate'].replace("low",4)
if (1 | 2 | 3 | 4) not in cardata['safetyrate']:
    print "Error: database column 'safety' has unidentified text. Text will be converted to rating 5."
    cardata['safetyrate'] = cardata['safetyrate'].replace("[a-z]|[A-Z]",5)
else:
    print "No errors."

#Create function to sort by column safetyrate
def sortbysafety(filename, input, size):
    """A function that sorts a list of objects based on their safety rating
    sort by descending high to low by default
    """
    if input == "asc":
        sort_asc = filename.sort_values('safetyrate', ascending=True)
        if size > 0:
            return sort_asc.head(size)
        else:
            print "Error, output size must be > 0"
    else:
        sort_dsc = filename.sort_values('safetyrate', ascending=False)
        if size > 0:
            return sort_dsc.head(size)
        else:
            print "Error, output size must  be > 0"

#run function to sort by safetyrate
sortbysafety(cardata, "des", 10)



#b. Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order 
#add new column for variable  maintrank
cardata['maintrank'] = cardata['maint'].replace("vhigh",1)
cardata['maintrank'] = cardata['maintrank'].replace("high",2)
cardata['maintrank'] = cardata['maintrank'].replace("med",3)
cardata['maintrank'] = cardata['maintrank'].replace("low",4)
if (1 | 2 | 3 | 4) not in cardata['maintrank']:
    print "Error: database column 'maint' has unidentified text. Text will be converted to rating 5."
    cardata['maintrank'] = cardata['maintrank'].replace("[a-z]|[A-Z]",5)
else:
    print "No errors."
    


#Create function to sort by column safetyrate
def sortbymaint(filename, input, size):
    """A function that sorts a list of objects based on their maintenace ranking
    sort by descending high to low by default
    """
    if input == "asc":
        sort_asc = filename.sort_values('maintrank', ascending=True)
        if size > 0:
            return sort_asc.head(size)
        else:
            print "Error, output size must be > 0"
    else:
        sort_dsc = filename.sort_values('maintrank', ascending=False)
        if size > 0:
            return sort_dsc.head(size)
        else:
            print "Error, output size must  be > 0"

#run function to sort by safetyrate
sortbymaint(cardata, "asc", 15)



#c. Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety'
#sorted by 'doors' in ascending order.  Find these matches using regular expressions. 
#filter for high/vhigh rows of buying, maint, and safety
highcardata = cardata.loc[cardata['buying'].str.contains(r'(high)')]
highcardata = highcardata.loc[cardata['maint'].str.contains(r'(high)')]
highcardata = highcardata.loc[cardata['safety'].str.contains(r'(high)')]
highcardata.head(5)

#Create function to sort by column doors
def sortbydoors(filename, input, size):
    """A function that sorts a list of objects based on their maintenace ranking
    sort by descending high to low by default
    """
    if input == "asc":
        sort_asc = filename.sort_values('doors', ascending=True)
        if size > 0:
            return sort_asc.head(size)
        else:
            print "Error, output size must be > 0"
    else:
        sort_dsc = filename.sort_values('doors', ascending=False)
        if size > 0:
            return sort_dsc.head(size)
        else:
            print "Error, output size must  be > 0"

#run function to sort by safetyrate
highcardata = sortbydoors(highcardata, "des", 10)



#d.Save to a file all rows (in any order) that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'persons': 4 or more.
#The file path can be a hard-coded location (name it output.txt) or use a dialog box.

cardata2d = cardata.loc[cardata['buying'].str.contains(r'(vhigh)')]
cardata2d = cardata2d.loc[cardata['maint'].str.contains(r'(med)')]
#I know this can be done using a method easier than regular expression but I wanted to give it a shot anyways
cardata2d = cardata2d.loc[cardata['doors'].str.contains(r'(4)')]
cardata2d = cardata2d.loc[cardata['persons'].str.contains(r'(4|more)')]
cardata2d.head(5)


cardata2d = tkFileDialog.asksaveasfilename(parent = root, initialfile = 'cardata2d', defaultextension = '.csv')
