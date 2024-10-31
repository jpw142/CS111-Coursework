#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year


    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def days_in_month(self):
        """ Returns the number of days in the called object's month
        """
        numdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.is_leap_year():
            numdays[2] = 29
            
        return numdays[self.month]    

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def day_name(self):
        """ Return the day of the week that the called Date object falls on. 
            IMPORTANT: This method won't work until you implement the 
            other methods of the class, as specified in Problem 1.
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        monday = Date(11, 20, 2023)
        num_days = self.days_between(monday)
        return day_names[num_days % 7]
    
    #### Put your code for the methods from Problem 1 below. ####
    #### Make sure that it is indented by an appropriate amount. ####

    def advance_one(self):
        """ advanced the date by 1 day """
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.year += 1
            self.month = 1

    def __eq__(self, rhs):
        """ determines if two dates are equal """
        return self.year == rhs.year and self.month == rhs.month and self.day == rhs.day

    def is_before(self, other):
        """ determines if a date is before another """
        if self.year > other.year:
            return False
        elif self.year < other.year:
            return True
        if self.month > other.month:
            return False
        elif self.month < other.month:
            return True
        if self.day > other.day:
            return False
        elif self.day < other.day:
            return True
        return False

    def is_after(self, other):
        """ determines if a date is before another """
        if self.is_before(other):
            return False
        if self == other:
            return False
        return True

    def days_between(self, other):
        """ determines the number of days between two dates """
        days = 0
        if self.is_before(other):
            factor = -1
            min = self.copy()
            max = other.copy()
        elif self.is_after(other):
            factor = 1
            min = other.copy()
            max = self.copy()
        else:
            return 0
        while min != max:
            min.advance_one()
            days += 1
        return days * factor

