#calulate entropy for a feature in our tennis example
from math import log2

def entropy(num_yes, num_no):
    total=num_yes+num_no
    prob_yes= num_yes/total
    prob_no=num_no/total
    HS= - prob_yes * log2(prob_yes) - prob_no*log2(prob_no)
    return HS



#wind H(Strong)
print("entropy for Wind Strong=", entropy(3,3))
print("entropy for Wind Weak=", entropy(6,2))

entropy_before_split= entropy(9,5)
print("entropy before split=", entropy_before_split)

entropy_after_split= 6/14 * entropy(3,3) + 8/14 * entropy(6,2)
print("entropy after split=", entropy_after_split)

print("Information Gain=",  entropy_before_split - entropy_after_split)
