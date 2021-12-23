import math as m
def log(a,b):
    """
    This function takes 2 arguments: base 'a' and argument 'b' for calculating the value of logarithm
    """
    if a>0 and b>0 and a!=1:
        return m.log(b,a)        
    else:
        return "Non-positive number, can't calculate the logarithm value"   

def ln(b):
    """
    This function takes 1 argument 'b' for calculating the value of natural logarithm (with the base e constant)
    """
    if b>0:
        a = m.e
        return m.log(b,a)
    else:
        return "Non-positive number, can't calculate the value of natural logarithm"       
    
def lg(b):
    """
    This function takes 1 argument 'b' for calculating the value of common logarithm (with the base 10)
    """
    if b>0:
        return m.log10(b)
    else:
        return "Non-positive number, can't calculate the logarithm value"   
    
