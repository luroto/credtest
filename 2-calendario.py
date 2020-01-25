#!/usr/bin/python3
'''
This module contains a function for calculating calendars

'''
if __name__ == "__main__":
    def calendar():
        meses = {1: 6, 2: 2, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4,
                 10: 6, 11: 2, 12: 4}
        leapyear = 0
        month = 0
        weekday = 0
        day = 1
        century = 1
        yy = 0
        leap = False
        suma = 0
        for year in range(1901, 2001):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap = True
                    else:
                        leap = False
                else:
                    leap = True
            else:
                leap = False
            if year >= 2000:
                century = 0
            yy = (year % 100) + int((year % 100) / 4)
            for mes in meses:
                if leap is True:
                    if mes == 1 or mes == 2:
                        leapyear = -1
                    else:
                        leapyear = 0
                month = meses[mes]
                weekday = (yy + leapyear + month + day + century) % 7
                if weekday == 0:
                    suma += 1

        print(("Entre el 1 de enero de 1901 y el 31 de diciembre del 2000" +
               ", hubo {:d} meses que iniciaron un domingo").format(suma))
    calendar()
