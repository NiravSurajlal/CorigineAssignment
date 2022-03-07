#!/usr/bin/env python3

import sys

def string_to_int(str_number):
    dig_map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    int_number = 0
    for digit in str_number:
        try:
            int_number = 10 * int_number + dig_map[digit]
        except Exception as e:
            print("The input must be am INTEGER, with no '.' etc.")
            return -1 
    return int_number

def calc_factorial(number, fac = 1):
    """ Takes an integer number and returns its factorial """
    
    while (number > 1):
        (number, fac) = (number - 1, fac * number)
    return fac

def calc_sum_of_digits(number, total = 0):
    """ Takes an integer number and returns the sum of its
        digits. """

    while (number > 9):
        # print (number)
        (number, total) = (number // 10, total + number % 10)

    # print (number)
    (number, total) = (number // 10, total + number % 10)
    return total

def main():
    factorial = calc_factorial(number)
    # print ("Factorial of {} is {}".format(number, factorial))
    sum_of_digits = calc_sum_of_digits(factorial)
    print (sum_of_digits)

if __name__ == "__main__":
    number = string_to_int(sys.argv[1])
    if number >= 0:
        main()
    else:
        print("Please try again.")
