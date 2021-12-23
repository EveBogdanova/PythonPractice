def root2(n):
    """
    This function takes the number n and returns it's square root
    """
    if n<0:
        return 'It is not positive number, so real value of square root is not defined'
    else:
        return n**0.5

def root3(n):
    """
    This function takes the number n and returns it's cube root
    """
    if n>=0:
        return round(n**(1/3),1)
    else:
        return round((-1)*(-n)**(1/3),1)
 