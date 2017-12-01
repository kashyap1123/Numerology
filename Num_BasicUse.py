"""
Num_BasicUse.py
~~~~~~~~~~~~~~~~~~~~~~

An example script to show basic use case for the numerology class
"""

from Num_BasicTypes import numerologybase
from datetime import datetime

# fname   = "Manjunath Kashyap"
# lname   = "Jataprolu"
# dob     = datetime(1988, 10, 03, 15, 25)
fname   = "Vaishnavi Kasyap"
lname   = "Jataprolu"
dob     = datetime(1991, 11, 18, 22, 30)

num_object  = numerologybase(fname, lname, dob)
print(num_object.name_first, num_object.name_last)
num_object.pop_dob_today_corr()
num_object.pop_age()
print('Age is ', num_object.age)
num_object.pop_birthnumber()
print('Birth Number is ', num_object.birth_number)
num_object.pop_progress_number()
print('Progress Number is ', num_object.progress_no)
num_object.pop_bad_years()
print('Bad years are ', num_object.bad_years)
num_object.pop_imp_years()
print('Imp years are ', num_object.imp_years)
