import re

def encode_crop_type(input):
    if(re.search('barley', input, re.IGNORECASE)):
        return 0
    elif(re.search('cotton', input, re.IGNORECASE)):
        return 1
    elif(re.search('ground nut', input, re.IGNORECASE)):
        return 2
    elif(re.search('maize', input, re.IGNORECASE)):
        return 3
    elif(re.search('millet', input, re.IGNORECASE)):
        return 4
    elif(re.search('oil seed', input, re.IGNORECASE)):
        return 5
    elif(re.search('paddy', input, re.IGNORECASE)):
        return 6
    elif(re.search('pulses', input, re.IGNORECASE)):
        return 7
    elif(re.search('sugarcane', input, re.IGNORECASE)):
        return 8
    elif(re.search('tobacco', input, re.IGNORECASE)):
        return 9
    elif(re.search('wheat', input, re.IGNORECASE)):
        return 10
    else:
        return None