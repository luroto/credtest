#!/usr/bin/python3
'''
This module contains a function which calculates pythagoric triplets
'''
if __name__ == "__main__":
    def euler():
        '''
        This function checks for the pythagoric triplet whose
        addition makes 1000
        '''
        a = 0
        b = 0
        c = 0
        prod = 0
        for i in range(3, 500):
            c = i*i
        for j in range(4, 500):
            b = j*j
        for k in range(5, 500):
            a = k*k
        suma = b + a
        if suma == c:
                if i + k + j == 1000:
                    prod = i*k*j
                    print(("Los numeros son {:d}, {:d} y {:d} y su suma " +
                           "es {:d}").format(k, j, i, (i + j + k)))
                    print(("El producto de esta tripleta pitagorica es {:d}").
                          format(prod))
                    return(0)

    euler()
