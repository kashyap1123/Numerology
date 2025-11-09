"""
Num_BasicUse.py
~~~~~~~~~~~~~~~~~~~~~~

An example script to show basic use case for the numerology class
"""

from Num_BasicTypes import numerologybase
from datetime import datetime


def run_numerology_example(fname, lname, dob):
	num_object = numerologybase(fname, lname, dob)
	print(f"\nNumerology for: {num_object.name_first} {num_object.name_last}")
	print("Date of Birth:", dob.date().strftime("%A %d. %B %Y"))
	num_object.pop_dob_today_corr()
	num_object.pop_age()
	print('Age:', num_object.age)
	num_object.pop_birthnumber()
	print('Birth Number:', num_object.birth_number)
	num_object.pop_progress_number()
	print('Progress Number:', num_object.progress_no)
	num_object.pop_bad_years()
	print('Bad years:', num_object.bad_years)
	num_object.pop_imp_years()
	print('Important years:', num_object.imp_years)
	num_object.pop_radical_years()
	print('Radical years:', num_object.radical_years)
	num_object.pop_zenith_years()
	print('Zenith years:', num_object.zenith_years)
	num_object.pop_birth_lom()
	print('Birth LoM:', num_object.birth_lom)
	num_object.pop_curr_lom()
	print('Current LoM:', num_object.curr_lom)
	print(num_object.print_chart())


if __name__ == "__main__":
	test_cases = [
		{"fname": "Manjunath Kashyap", "lname": "Jataprolu", "dob": datetime(1988, 10, 3, 15, 25)},
	#	{"fname": "Vaishnavi Kasyap", "lname": "Jataprolu", "dob": datetime(1991, 11, 18, 22, 30)},
	#	{"fname": "Shreyas", "lname": "", "dob": datetime(1990, 1, 11, 5, 45)},
	]
	for case in test_cases:
		run_numerology_example(case["fname"], case["lname"], case["dob"])
