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
from Num_LoMHelper import Num_LoMHelper
from Num_ChartHelper import Num_ChartHelper

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

# We note that singling is just the iterative mapping from {0,,10} to {0,,9}
# as such a quick way to single is just take remainder wrt 9
def single_quick(nums):
    return(sum(nums)%9)

def doublle(nums):
    """
    Take a list of numbers and double <=> their sum (these commute).
    Doubling is defined as recursively summing digits till you end up with
    a single digit.
    """
    temp_sum    = 0
    numsum      = sum(nums)
    for digit in str(numsum):
        temp_sum       += int(digit)
    return(temp_sum)

def lom(date):
    # This needs to be implemented
    return(0)

def bad_years(dob):
    age_latest          = 0
    age_latest_diff     = 0
    year_curr           = dob.year
    imp_years           = []

    while age_latest < 100:
        age_latest_diff  = doublle([year_curr])
        year_curr   = year_curr + age_latest_diff
        age_latest  += age_latest_diff
        imp_years.append(year_curr)

    return(imp_years)

def imp_years(dob):
    age_latest          = 0
    age_latest_diff     = 0
    year_curr           = dob.year
    imp_years           = []

    while age_latest < 100:
        age_latest_diff  = single([year_curr])
        year_curr   = year_curr + age_latest_diff
        age_latest  += age_latest_diff
        imp_years.append(year_curr)

    # Note that the above is essentially singling a GP and can be implemented
    # as such. However, that lacks clarity and so we choose the above

    return(imp_years)

def radical_years(dob,bno):
    a0  = single([dob.year])
    a1  = bno - a0
    if (a1<1):
        a1  += 9

    return(range(dob.year + a0, dob.year + a0 + 100, 9))

def zenith_years(dob):
    z1  = dob.year + single([dob.day, dob.month]) + doublle([dob.year])
    z2  = z1 + dob.day
    z3  = z2 + dob.month
    return([z1,z2,z3])

class numerologybase:
    """Class to hold all the relevant numerological metrics and details for
    an individual """
    def __init__(self, fname, lname, dob):
        self.name_first = fname
        self.name_last  = lname
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
        self.curr_lom       = 0
        self.progress_no    = 0
        self.bad_years      = []
        self.imp_years      = []
        self.radical_years  = []
        self.zenith_years   = []

        self.lom_helper     = Num_LoMHelper(self.dob_corr)
        self.chart_helper   = Num_ChartHelper(self.dob_corr)

    def pop_dob_today_corr(self):
        timeshift                   = timedelta(hours=12)
        temp_dob_datetime_corr      = self.dob - timeshift
        temp_today_datetime_corr    = self.now - timeshift
        self.dob_corr               = temp_dob_datetime_corr.date()
        self.today_corr             = temp_today_datetime_corr.date()
        self.lom_helper.dob_corr    = self.dob_corr
        self.chart_helper.dob_corr  = self.dob_corr

    def pop_age(self):
        days_diff           = self.today_corr - self.dob_corr
        self.age            = (days_diff.days)/365     # Needsnto be more accurate

    def pop_birthnumber(self):
        list_dob            = [self.dob_corr.day, self.dob_corr.month, (self.dob_corr.year)%100]
        self.birth_number   = single(list_dob)

    # Need to complete this
    def pop_birth_lom(self):
        self.pop_dob_today_corr()
        self.lom_helper.pop_birth_lom()
        self.birth_lom      = self.lom_helper.birth_lom

    def pop_progress_number(self):
        # Procedure laid out below is valid only for birthday (curr) till EoY
        # For SoY till next birthday, it is (axiomatically) + 1
        # So we compute based on preceding b'day and adjust if needed
        adjust  = 0
        if (self.dob_corr.month>self.today_corr.month):
            adjust  = 1
        elif (self.dob_corr.month==self.today_corr.month):
            if (self.dob_corr.day>self.today_corr.day):
                adjust  = 1

        curr_year_adjust    = self.today_corr.year - adjust

        # Step 1. Repeat Birth Number procedure with current year
        a1  = single([self.dob_corr.day, self.dob_corr.month, (curr_year_adjust)%100])
        # Step 2. Subtract YoB from current years. Note this is not always=age
        a2  = curr_year_adjust - self.dob_corr.year
        # Step 3. Double this and single digits
        a3  = single([a2 * 2])
        # Step 4. Add this to YoB
        a4  = self.dob_corr.year + a3
        # Step 5. Single the digits of the year
        a5  = single([a4])
        # Step 6. Add a1 and a5
        a6  = a1 + a5

        # Now adjust if needed
        self.progress_no    = single([a6 + adjust])
        # Can write a test to check that progress numbers increase by 3 every yr

    def pop_curr_lom(self):
        # First make sure progress_no is computed, we need it
        self.pop_progress_number()
        self.curr_lom   = single([self.progress_no, lom(self.today_corr)])

    def pop_bad_years(self):
        self.bad_years  = bad_years(self.dob_corr)

    def pop_imp_years(self):
        self.imp_years  = imp_years(self.dob_corr)

    def pop_radical_years(self):
        self.pop_birthnumber()
        self.radical_years  = radical_years(self.dob_corr, self.birth_number)

    def pop_zenith_years(self):
        self.zenith_years   = zenith_years(self.dob_corr)

    def print_chart(self):
        self.chart_helper.print_chart()

# for debug, remove once done
print("done")
