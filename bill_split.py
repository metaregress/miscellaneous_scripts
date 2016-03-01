# A script to keep me from having to calculate rent by hand

import sys

RENT_BASE = 1797
RENT_SPLIT = RENT_BASE / 2

bill_1 = float(sys.argv[1])
bill_2 = float(sys.argv[2])
bill_3 = float(sys.argv[3])

bill_total = (bill_1 + bill_2 + bill_3)
bill_split = bill_total / 2
round_split = round(bill_split)

plus_split = RENT_SPLIT + round_split
minus_split = RENT_SPLIT - round_split


print("Bills total: " + str(bill_total))
print("Split two ways: " + str(bill_split))
print("Call it " + str(round_split))

print("Rent plus split: " + str(plus_split))
print("Rent minus split: " + str(minus_split))