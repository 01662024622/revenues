from Entity.ht50_revenues import Revenues


def sumOfMonth(row: Revenues):
    return row.t1 + row.t2 + row.t3 + \
           row.t4 + row.t5 + row.t6 + \
           row.t7 + row.t8 + row.t9 + \
           row.t10 + row.t11 + row.t12


def checkLevel(value: int):
    if value >= 2000000000:
        return "Platinum"
    elif value >= 1000000000:
        return "Gold"
    elif value >= 500000000:
        return "Titan"
    elif value >= 200000000:
        return "Silver"
    else:
        return "Member"


class Calculation:
    def __init__(self, month):
        self.month = month

    def setValue(self, shallow, value):
        if self.month == 1:
            shallow.t1 = value
            return shallow
        if self.month == 2:
            shallow.t2 = value
            return shallow
        if self.month == 3:
            shallow.t3 = value
            return shallow
        if self.month == 4:
            shallow.t4 = value
            return shallow
        if self.month == 5:
            shallow.t5 = value
            return shallow
        if self.month == 6:
            shallow.t6 = value
            return shallow
        if self.month == 7:
            shallow.t7 = value
            return shallow
        if self.month == 8:
            shallow.t8 = value
            return shallow
        if self.month == 9:
            shallow.t9 = value
            return shallow
        if self.month == 10:
            shallow.t10 = value
            return shallow
        if self.month == 11:
            shallow.t11 = value
            return shallow
        if self.month == 12:
            shallow.t12 = value
            return shallow


