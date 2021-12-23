import factorial.factorial as f
import exp_root.exponentiation as exp
import exp_root.root as rt
import logarithm.logarithm as lm

def main():
    print('\nThis programm allows you to test all the functions from created packages\n')
    print('---------------------- MENU ----------------------------\n\n1) calculating factorial value ---> fact() function\n2) calculating value of squared number ---> exp2() function\n3) calculating value of cubed number ---> exp3() function\n4) calculating value of square root ---> root2() function\n5) calculating value of cube root ---> root3() function\n6) calculating value of logarithm (you choose the base and the argument) ---> log() function\n7) calculating value of natural logarithm (with the base e constant) ---> ln() function\n8) calculating value of common logarithm (with the base 10) ---> lg() function\n\nEXIT ---> 27')
    choose = True
    while choose == True:
        try:
            test = int(input('\nChoose the number of function you would like to test: '))
            if test == 1:
                number = int(input('\nEnter a number for calculating factorial: '))
                print(f'\nFactorial value for {number} is: {f.fact(number)}')
            elif test == 2:
                number = int(input('\nEnter a number to square it: '))
                print(f'\n{number} squared is: {exp.exp2(number)}')
            elif test == 3:
                number = int(input('\nEnter a number to cube it: '))
                print(f'\n{number} cubed is: {exp.exp3(number)}')  
            elif test == 4:
                number = int(input('\nEnter a number to get a square root: '))
                print(f'\nThe square root of {number} is: {rt.root2(number)}')
            elif test == 5:
                number = int(input('\nEnter a number to get a cube root: '))
                print(f'\nThe cube root of {number} is: {rt.root3(number)}')
            elif test == 6:
                base = int(input('\nEnter a base of logarithm: '))
                arg = int(input('\nEnter an argument of logarithm: '))
                print(f'\nThe logarithm with the base {base} and argument {arg} is: {lm.log(base,arg)}')
            elif test == 7:
                arg = int(input('\nEnter an argument of natural logarithm: '))
                print(f'\nThe value of natural logarithm with argument {arg} is: {lm.ln(arg)}')
            elif test == 8:
                arg = int(input('\nEnter an argument of common logarithm: '))
                print(f'\nThe value of common logarithm with argument {arg} is: {lm.lg(arg)}')                      
            elif test == 27:
                choose = False
        except ValueError:
            print('\nPlease, choose the proper number')
            continue    
    return 'Thanks for your attention'    

print(main())   