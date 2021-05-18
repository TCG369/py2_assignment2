"""
Assignment 4 // ATM // Shawn Cote
"""
import sys

def main():

    """
    User has to choose 1234 as PIN. If they fail 3 times, they get locked out.
    """

    validpin = 1234
    count = 0
    maximum = 3


    while count < maximum:
        try:
            count += 1
            userpin = int(input('\nPlease enter your PIN: '))
            if userpin == validpin:
                print('\nYour account balance is: $0.00. You are Broke! Goodbye!\n')
                sys.exit()
            elif count == maximum:
                print('\nInvalid Pin.\n\nAccount locked! The Police have been notified!\n')
                break
            else:
                print('\nInvalid Pin')
        except ValueError:
            if count == maximum:
                print('\nInvalid Pin.\n\nAccount locked! The Police have been notified!\n')
                break
            print('\nInvalid Pin')





if __name__ == '__main__':
    main()
