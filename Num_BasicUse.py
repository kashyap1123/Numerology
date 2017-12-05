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
# fname   = "Vaishnavi Kasyap"
# lname   = "Jataprolu"
# dob     = datetime(1991, 11, 18, 22, 30)
fname   = "Shreyas"
lname   = ""
dob     = datetime(1990, 01, 11, 05, 45)

num_object  = numerologybase(fname, lname, dob)
print(num_object.name_first, num_object.name_last)
print("Date of Birth is ", dob.date().strftime("%A %d. %B %Y"))
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
num_object.pop_radical_years()
print('Radical years are ', num_object.radical_years)
num_object.pop_zenith_years()
print('Zenith years are ', num_object.zenith_years)
num_object.pop_birth_lom()
print('Birth LoM is ', num_object.birth_lom)
num_object.pop_curr_lom()
print('Current LoM is ', num_object.curr_lom)
