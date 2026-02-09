import sys
import string
from collections import Counter

S = input()

counter = Counter(S)

lower_set = set(string.ascii_lowercase)
upper_set = set(string.ascii_uppercase)

is_upper = False
is_lower = False
for k, v in counter.items():
    if v > 1:
        print("No")
        sys.exit()
    if k in lower_set:
        is_lower = True
    elif k in upper_set:
        is_upper = True

if is_lower and is_upper:
    print("Yes")
else:
    print("No")
