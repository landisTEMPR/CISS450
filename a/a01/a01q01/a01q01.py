# ===========================
# File : a01q01.py
# Author : Brysen Landis
# ===========================


def matrix(n, s, separator=','):

    pass

if __name__ == '__main__':
    n = int(intput())                       # for instance enter 3
    s = input()                             # for instance enter "a, b, c, d, e, f, g, h, i"

    separator = input()                     # for instance enter ","
                                            # or enter "" for default case
    if separator == '':                     
        print(matrix(n=n, s=s))
    else:
        print(matrix(n=n, s=s, separator=separator))
