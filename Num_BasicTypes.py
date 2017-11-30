"""
Num_BasicTypes.py
~~~~~~~~~~~~~~~~~~~~~~

Some basic data types and routines for numerology.

We define a DoB holder. Now on top of this, we will have a data type to hold all
important metrics that we compute - for example, progress number, radical years,
etc.,

We will then define getters for computing these."""

#### Libraries
# Standard library

from datetime import datetime as dt
from datetime import timedelta

# Take a list of numbers and single <=> their sum (these commute)
# Singling is defined as recursively summing digits till you end up with
# a single digit
def single(nums):
    c = []
    numsum  = str(sum(nums))
    for digit in numsum:
        c.append(int(digit))

    if (len(c) == 1):
        res = c[0]
    else:
        res = single(c)

    return(res)

class numerologybase:
    """Class to hold all the relevant numerological metrics and details for
    an individual """
    def __init__(self, fname, lname, dob):
        self.name_first = fname
        self.name_Last  = lname
        self.dob        = dob
        self.dob_corr   = dob.date()
        self.now        = dob.today()
        self.today_corr = dob.date()

        # Name_First      = str("")
        # Name_Last       = str("")
        # DoB             = dt(2017, 12, 01, 12, 30)

        self.age            = 0
        self.birth_number   = 0
        self.birth_lom      = 0
        self.bad_years      = []
        self.imp_years      = []
        self.radical_years  = []
        self.zenith_years   = []

    def pop_dob_today_corr(self):
        timeshift                   = timedelta(hours=12)
        temp_dob_datetime_corr      = self.dob - timeshift
        temp_today_datetime_corr    = self.now - timeshift
        self.dob_corr               = temp_dob_datetime_corr.date()
        self.today_corr             = temp_today_datetime_corr.date()

    def pop_age(self):
        days_diff           = self.today_corr - self.dob_corr
        self.age            = (days_diff.days)/365     # Needsnto be more accurate

    def pop_birthnumber(self):
        list_dob            = [self.dob_corr.day, self.dob_corr.month, (self.dob_corr.year)%100]
        self.birth_number   = single(list_dob)

# for debug, remove once done
print("done")
