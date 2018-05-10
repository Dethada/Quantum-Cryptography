#!/usr/bin/env python3
from random import randint
from math import gcd
from sys import argv

# finds the multiplicative order of a mod n
# https://stackoverflow.com/a/642533
def multiplicative_order(a, n):
    if gcd(a, n) > 1:
        return 0
    else:
        order = 1
        mod_exp = a
        while mod_exp != 1:
            order += 1
            mod_exp = (mod_exp * a) % n
        return order


def solve(n):
    while True:
        # Step 1
        # starts from 2 because 1 power anything is 1
        x = randint(2, n-1)
        tmp = gcd(x,n)
        if tmp != 1:
            print('We got lucky! Factor of {} is {} and {}!'.format(n, tmp, n//tmp))
            return [tmp, n//tmp]
        print('Generated random integer x: {}'.format(x))

        # Step 2
        # In actual shor's algorithm quantum fourier transform will be implemented here.
        r = multiplicative_order(x, n)
        print('Multiplicative Order of {} mod {} => {}'.format(x, n, r))

        # Step 3
        if r % 2 != 0:
            print('{} is not even :( going back to first step...\n'.format(r))
            continue
        elif (x**(r//2)+1) % n == 0:
            print('{} is a multiple of n :( back to first step...\n'.format(r))
            continue
        else:
            factor1 = gcd(n, (x**(r//2)+1))
            factor2 = gcd(n, (x**(r//2)-1))
            return [factor1, factor2]


def main():
    if len(argv) != 2:
        print('Usage: {} <number>'.format(argv[0]))
        return
    try:
        n = int(argv[1])
    except ValueError:
        print('Invalid input')
        return
    if n <= 2:
        print('n is too small!')
        return
    factors = solve(n)
    print('Factor of {} is {} and {}\n'.format(n, factors[0], factors[1]))


if __name__ == '__main__':
    main()
