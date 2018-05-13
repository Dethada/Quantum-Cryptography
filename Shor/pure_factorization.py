#!/usr/bin/env python3
from math import sqrt
from sys import argv

# returns all factors of x except for 1 and x itself
# O(sqrt(N)/2)
def factorize(x):
    if x % 2 == 0:
        return [2, x // 2]
    for i in range(3, int(sqrt(x))+1, 2):
        if (x % i == 0):
            return [i, x // i]

# print(factorize(2978273257))
def main():
    if len(argv) != 2:
        print('Usage: {} <number>'.format(argv[0]))
        return
    try:
        print(factorize(int(argv[1])))
    except ValueError:
        print('Invalid number!')
        return

if __name__ == '__main__':
    main()
