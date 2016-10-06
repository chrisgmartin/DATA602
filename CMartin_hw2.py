#1. fill in this class
#   it will need to provide for what happens below in the
#    main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
#     a function called showEvaluation, and an attribute carCount
class CarEvaluation(object):
    """A simple class that represents a car evaluation
    the class is made up of a brand, price (categorical), and safety_rating (numerical)
    """
    carCount = 0
    def __init__ (self, brand, price, safety_rating):
        self.brand = brand
        self.price = price
        self.safety_rating = safety_rating
        type(self).carCount += 1
    def showEvaluation(self):
        """displays the attributes of the object in sentance form"""
        print "The", self.brand, "has a", self.price, "price and it's safety is rated a", self.safety_rating
    def __repr__(self):
        """displays the characteristics of the item"""
        return "<brand: %s, price: %s, safety rating: %s>" % (self.brand, self.price, self.safety_rating)


#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
#     otherwise by descending price
def sortbyprice(list, input):
    """A function that sorts a list of objects based on their price
    assigns a new attribute price_rank (high price = 1, low = 3)
    sort by descending high to low by default
    """
    for i in list:
        if i.price == 'High':
            i.price_rank = 1
        elif i.price == 'Med':
            i.price_rank = 2
        elif i.price == 'Low':
            i.price_rank = 3
        else:
            continue
    
    if input == "asc":
        car_list = sorted(list, key = lambda x: x.price_rank, reverse = True)
    else:
        car_list = sorted(list, key = lambda x: x.price_rank)
    return [car.brand for car in car_list]



#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#    it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
def searchforsafety(list, rating):
    """search for the safety rating within the list
    if the safety rating is found in the list, a TRUE is returned, else a FALSE is returned
    """
    safety_rating_list = [cars.safety_rating for cars in L]
    if rating in safety_rating_list:
        return "True"
    return "False"
    

# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount  # Car Count = 3

    eval1.showEvaluation()  # The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation()  # The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation()  # The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc");  # [Toyota, GMC, Ford]
    print sortbyprice(L, "des");  # [Ford, GMC, Toyota]
    print searchforsafety(L, 2);  # true
    print searchforsafety(L, 1);  # false
