"""
Num_BasicUse.py
~~~~~~~~~~~~~~~~~~~~~~

An example script to show basic use case for the numerology class
"""

from Num_BasicTypes import numerologybase
from datetime import datetime

fname   = "Manjunath Kashyap"
lname   = "Jataprolu"
dob     = datetime(1988, 10, 03, 15, 25)

num_object  = numerologybase(fname, lname, dob)
num_object.pop_dob_today_corr()
num_object.pop_age()
print('Age is ', num_object.age)
num_object.pop_birthnumber()
print('Birth Number is ', num_object.birth_number)
