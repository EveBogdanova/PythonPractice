
def fact(n):
    """
    The function for calculating the factorial value for natural number
    """
    if type(n) == int and n>0:
        if n == 0 or n == 1:
            return 1
        else:
            return n* fact(n-1)
    else:
        return 'Not natural number'