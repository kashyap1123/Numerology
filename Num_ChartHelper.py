"""
Num_ChartHelper.py
~~~~~~~~~~~~~~~~~~~~~~

Some basic routines for Numerological Chart Calculations.
The Standard numerological chart looks as follows:

============================================================
            || Domestic     || Financial    || In-Laws
============================================================
Philosophy  ||  3           ||  1           ||  9
============================================================
Education   ||  6           ||  7           ||  5
============================================================
Wealth      ||  2           ||  8           ||  4
============================================================
"""

class Num_ChartHelper:
    """docstring for Num_ChartHelper."""
    def __init__(self, dob_corr):
        self.dob_corr   = dob_corr

    def pop_cardin(self):
        dob_str = str(self.dob_corr.day) + str(self.dob_corr.month) \
                  + str(self.dob_corr.year)
        # print(dob_str)
        self.cardinal = {x : dob_str.count(str(x)) for x in range(1, 10, 1)}
        # print("cardinality", self.cardinal)

    def print_chart(self):
        # Print the num chart in the format shown in the header
        # First force check frequency population
        self.pop_cardin()
        line_len    = 80
        col_width   = line_len/4
        rule        = "=" * line_len
        sep         = "||"

        vert        = ["", "Domestic", "Financial", "In-Laws" ]
        horiz       = ["Philosophy", "Education", "Wealth"]
        # List order per chart
        order       = [ [3, 1, 9], [6, 7, 5], [2, 8, 4]]
        # Print each number its frequency number of times
        order_fill  = map(lambda y : map(lambda x : str(x) * self.cardinal[x], y), order)

        print("\n")
        print(rule)
        print("Numerical Chart...")
        print("\n")
        print(rule)
        print sep.join(word.ljust(col_width) for word in vert )

        for i, arr in enumerate(order_fill):
            arr.insert(0,horiz[i])
            print(rule)
            print sep.join(word.ljust(col_width) for word in arr )
        print(rule)
