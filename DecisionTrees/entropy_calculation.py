# calulate entropy for each feature in
# our should we play tennis example
from math import log2

def entropy(num_yes, num_no):
    total=num_yes+num_no
    
    prob_yes= num_yes/total
    prob_no=num_no/total

    HS=0
    if prob_yes > 0:
        HS-= prob_yes * log2(prob_yes)
    if prob_no > 0:
        HS-= prob_no*log2(prob_no)
    return HS

#Wind Information Gain
print("entropy for Wind Strong=", entropy(3,3))
print("entropy for Wind Weak=", entropy(6,2))

entropy_before_split= entropy(9,5)
print("entropy before split=", entropy_before_split)

entropy_after_split= 6/14 * entropy(3,3) + 8/14 * entropy(6,2)
print("entropy after split=", entropy_after_split)

print("Information Gain=",  entropy_before_split - entropy_after_split)

#Humidity Information Gain 
print("\nentropy for Humidity High=", entropy(3,4))
print("entropy for Humidity Normal=", entropy(6,1))

entropy_after_split= 7/14 * entropy(3,4) + 7/14 * entropy(6,1)
print("entropy after split=", entropy_after_split)

print("Humidity split Information Gain=",  entropy_before_split - entropy_after_split)

#Outlook Information Gain 
print("\nentropy for Outlook Sunny=", entropy(2,3))
print("entropy for Outlook Overcast=", entropy(4,0))
print("entropy for Outlook Rain=", entropy(3,2))

entropy_after_split= 5/14 * entropy(2,3) + 4/14 * entropy(4,0) + 5/14*entropy(3,2)
print("entropy after split=", entropy_after_split)

print("Outlook split Information Gain=",  entropy_before_split - entropy_after_split)


#Temp Information Gain 
print("\nentropy for Temp Sunny=", entropy(2,2))
print("entropy for Temp Overcast=", entropy(4,2))
print("entropy for Temp Rain=", entropy(3,1))

entropy_after_split= 4/14 * entropy(2,2) + 6/14 * entropy(4,2) + 4/14*entropy(3,1)
print("entropy after split=", entropy_after_split)

print("Temp split Information Gain=",  entropy_before_split - entropy_after_split)

