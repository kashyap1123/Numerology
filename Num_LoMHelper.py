"""
Num_LoMHelper.py
~~~~~~~~~~~~~~~~~~~~~~

Some basic routines for Lord of Month Calculations.
"""

def birth_lom(dob):
    date_pairs  = [(1, 21), (2, 21), (3, 21), (4, 21), (5, 21), (6, 21), (7, 5),\
                  (7, 21), (8, 5), (8, 21), (9, 21), (10, 21), (11, 21), (12, 21)]
    lom_list    = [8, 8, 3, 9, 6, 5, 2, 7, 1, 4, 5, 6, 9, 3]
    month       = dob.month
    day         = dob.day
    match_ind   = [i for i, x in enumerate(date_pairs) if (month, day) < x]
    if(len(match_ind) == 0):
        birth_lom   = lom_list[0]
    else:
        birth_lom   = lom_list[match_ind[-1]]
    return(birth_lom)

class Num_LoMHelper:
    """Class to hold the Lord of Month and related Calculations
    """
    def __init__(self, dob_corr):
        self.dob_corr   = dob_corr
        self.birth_lom  = 0

    def pop_birth_lom(self):
        self.birth_lom  = birth_lom(self.dob_corr)
