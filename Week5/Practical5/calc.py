def calculate_cube(x):
    return x**3

def calculate_square(y):
    return y*y 

import pretty_print 
def main():
    result=calculate_square(2)
    pretty_print.simple_print(result)

    result1=calculate_cube(4)
    pretty_print.pro_print(result1)

main()