# An implementation of a decision tree.
# Should I play tennis today?
#
# The decision is based on weather outlook, humidity and wind strength
#
outlook=(input('What is the outlook?(sunny/overcast/rainy)')).lower()
if outlook == 'sunny':
    humidity=input('What is the humidity?(high/normal)')
    if humidity == 'high':
        print('No tennis today')
    else:
        print('Yes, play tennis')
elif outlook == 'overcast':
    print('Yes, play tennis')
else:
    wind=input('What is the wind strength?(high/normal)')
    if wind == 'high':
        print('No tennis today')
    else:
        print('Yes, play tennis')
