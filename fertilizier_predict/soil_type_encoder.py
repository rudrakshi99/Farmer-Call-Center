import re

def encode_soil_type(input):
    if(re.search('black', input, re.IGNORECASE)):
        return 0
    elif(re.search('clay', input, re.IGNORECASE)):
        return 1
    elif(re.search('loamy', input, re.IGNORECASE)):
        return 2
    elif(re.search('red', input, re.IGNORECASE)):
        return 3
    elif(re.search('sandy', input, re.IGNORECASE)):
        return 4
    else:
        return None