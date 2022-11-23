def decode_fertilizer(input):
    if(input == 0):
        return '10-26-26'
    elif(input == 1):
        return '14-35-14'
    elif(input == 2):
        return '17-17-17'
    elif(input == 3):
        return '20-20'
    elif(input == 4):
        return '28-28'
    elif(input == 5):
        return 'DAP'
    elif(input == 6):
        return 'Urea'
    else:
        return None