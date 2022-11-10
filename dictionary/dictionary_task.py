#  function that takes a roman numeral and converts it to an integer

def var_of_roman(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

def back_to_decimal(str):
    res = 0
    i = 0

    while (i < len(str)):
        # Fetch the index i of s, i.e s[i]
        s1 = var_of_roman(str[i])
        if (i + 1 <len(str)):
            # Fetch increment value of index in s[i + 1]
            s2 = var_of_roman(str[i + 1])
            
            if (s1 >= s2):
                res += s1
                i += 1
            else:
                res += s2 - s1
                i = i + 2
        else:
            res += s1
            i += 1
    return res

print('The value of  III is ', back_to_decimal('III'))
print('The value of LVIII is ',back_to_decimal('LVIII'))
print('The value of MCMXCIV is ',back_to_decimal('MCMXCIV'))
print('The value of XCIX is ',back_to_decimal('XCIX'))
print('The value of MMDCCCL is ',back_to_decimal('MMDCCCL'))