##
##after 2+ yrs of semicolon usage i wanted to try out this bad guy
##

import random
import string

LET = string.ascii_letters
NUM = string.digits
PUN = string.punctuation
ARR = LET + NUM + PUN
pw = ''

length = input("Length of the pw: \n")
length = int(length)

for c in range(length):
	pw += random.choice(ARR)
print(pw)
