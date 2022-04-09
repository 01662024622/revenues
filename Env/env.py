class Env:
    def __init__(self, month):
        self.month = month

        self.rangeMonth = ["",
                           "r.DocDate>='2022-01-01' and r.DocDate<'2022-02-01'",
                           "r.DocDate>='2022-02-01' and r.DocDate<'2022-03-01'",
                           "r.DocDate>='2022-03-01' and r.DocDate<'2022-04-01'",
                           "r.DocDate>='2022-04-01' and r.DocDate<'2022-05-01'",
                           "r.DocDate>='2022-05-01' and r.DocDate<'2022-06-01'",
                           "r.DocDate>='2022-06-01' and r.DocDate<'2022-07-01'",
                           "r.DocDate>='2022-07-01' and r.DocDate<'2022-08-01'",
                           "r.DocDate>='2022-08-01' and r.DocDate<'2022-09-01'",
                           "r.DocDate>='2022-09-01' and r.DocDate<'2022-10-01'",
                           "r.DocDate>='2022-10-01' and r.DocDate<'2022-11-01'",
                           "r.DocDate>='2022-11-01' and r.DocDate<'2022-12-01'",
                           "r.DocDate>='2022-12-01' and r.DocDate<'2023-01-01'",
                           ]

    def getRangeMoth(self):
        return self.rangeMonth[self.month]

    def getMonth(self):
        return "t" + self.month

