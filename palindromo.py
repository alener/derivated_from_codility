


def ispalindrom(p1,p2):
    xor_sum = 0
    for letter in p1:
        letter = ord(letter)
        xor_sum = xor_sum^letter
    for letter in p2:
        letter = ord(letter)
        xor_sum = xor_sum^letter
    if xor_sum == 0:
        return True
    else:
        return False
        
    

