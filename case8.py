"""Case-study #8 Data visualization
Developers:
Matyukhina Liza(20%), Rashidova Aigerim(60%), Romanenko Alina(0%)"""

import numpy as np
import matplotlib.pyplot as plt
from math import *
from ru_local import *


def usd_dynamics():
    """A graph of the dynamics of the USD."""
    usd = []
    days = []
    day = 1
    with open('usd.txt') as f_in:
        for i in f_in:
            usd.append(float(i))
            days.append(day)
            day += 1
    plt.plot(days, usd)
    plt.show()


def exchange_rates():
    """Graphs of the dynamics of several currencies."""
    usd = []
    euro = []
    aus = []
    days = []
    day = 1
    with open('usd_euro_aus.txt') as f_in:
        for i in f_in:
            days.append(day)
            a, b, c = i.split()
            usd.append(float(a))
            euro.append(float(b))
            aus.append(float(c))
            day += 1
    plt.plot(days, usd, days, euro, days, aus)
    plt.show()


def finalization_of_graphs():
    """Adding service information and displaying the grid."""
    usd = []
    euro = []
    aus = []
    days = []
    day = 1
    with open('usd_euro_aus.txt') as f_in:
        for i in f_in:
            days.append(day)
            a, b, c = i.split()
            usd.append(float(a))
            euro.append(float(b))
            aus.append(float(c))
            day += 1
    plt.plot(days, usd, days, euro, days, aus)
    plt.xlabel(DAYS)
    plt.ylabel(CURRENCY_RATE)
    plt.title(r'$f_1=USD, f_2=euro, f_3=AUD$')
    plt.grid(True)
    plt.show()


def several_graphs():
    """Displaying multiple charts for each currency."""
    usd = []
    euro = []
    aus = []
    days = []
    day = 1
    with open('usd_euro_aus.txt') as f_in:
        for i in f_in:
            days.append(day)
            a, b, c = i.split()
            usd.append(float(a))
            euro.append(float(b))
            aus.append(float(c))
            day += 1

    # subplot 1
    plt.subplot(221)
    plt.plot(days, usd)
    plt.ylabel(CURRENCY_RATE)
    plt.title(r'$USD$')
    plt.grid(True)

    # subplot 2
    plt.subplot(222)
    plt.plot(days, euro, 'g')
    plt.ylabel(CURRENCY_RATE)
    plt.title(r'$euro$')
    plt.grid(True)

    # subplot 3
    plt.subplot(223)
    plt.plot(days, aus, 'r')
    plt.ylabel(CURRENCY_RATE)
    plt.title(r'$AUD$')
    plt.grid(True)
    plt.show()


def coordinate_system():
    """Graphs in the polar coordinate system."""
    dat = []
    dat_ = []
    money = []
    money_ = []
    month = 1
    summ = 0
    days = 0
    month_ = 0
    plt.subplot(111, polar=True)
    with open('input5.txt') as f_in:
        for item in f_in:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money.append(summ / days)
                dat.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat, money, lw=2)

    month = 1
    days = 0
    month_ = 0
    with open('input5_2.txt') as f_in2:
        for item in f_in2:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money_.append(summ / days)
                dat_.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat_, money_, lw=2)
    plt.show()


def labels():
    """Using labels in the graphs."""
    dat = []
    dat_ = []
    money = []
    money_ = []
    month = 1
    summ = 0
    days = 0
    month_ = 0
    plt.subplot(111, polar=True)
    with open('input5.txt') as f_in:
        for item in f_in:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money.append(summ / days)
                dat.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat, money, lw=2)

    month = 1
    days = 0
    month_ = 0

    with open('input5_2.txt') as f_in2:
        for item in f_in2:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money_.append(summ / days)
                dat_.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat_, money_, lw=2)
    plt.title('Currency, USD and Euro')
    plt.ylabel('Rubles')
    plt.xlabel('Rubles')
    plt.show()


def different_points():
    """Types of points in the graphs."""
    dat = []
    dat_ = []
    money = []
    money_ = []
    month = 1
    summ = 0
    days = 0
    month_ = 0
    plt.subplot(111, polar=True)
    with open('input5.txt') as f_in:
        for item in f_in:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money.append(summ / days)
                dat.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat, money, lw=2)

    month = 1
    days = 0
    month_ = 0

    with open('input5_2.txt') as f_in2:
        for item in f_in2:
            if int(item[3:5]) == month:
                date, _mon = item.split()
                summ += float(_mon)
                days += 1
            else:
                money_.append(summ / days)
                dat_.append(month_ * pi / 6)
                summ = 0
                month_ += 1
                month += 1
                days = 0
    plt.plot(dat_, money_, 'bs')
    plt.title('Currency')
    plt.show()


def gistogram():
    """Presentation of data in a bar graph."""
    objects = (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
    y_pos = np.arange(len(objects))
    performance = []
    with open('input11.txt') as f_in:
        for i in f_in:
            performance.append(float(i))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel(RUB)
    plt.title(USD_KURS)
    plt.show()


def diagram():
    """The volume of transactions for the purchase of USD and euros for rubles."""
    data = [1036.4, 1500]
    plt.figure(num=1, figsize=(6, 6))
    plt.axes(aspect=1)
    plt.title(VOLUME_OF_DEALS, size=14)
    plt.pie(data, labels=(USD, EURO))
    plt.show()


def main():
    try:
        n = int(input(ENTER_TASK_NUMBER))
        if n == 1:
            usd_dynamics()
        elif n == 2:
            exchange_rates()
        elif n == 3:
            finalization_of_graphs()
        elif n == 4:
            several_graphs()
        elif n == 5:
            coordinate_system()
        elif n == 8:
            labels()
        elif n == 9:
            different_points()
        elif n == 11:
            gistogram()
        elif n == 12:
            diagram()
        else:
            print(SORRY)
    except ValueError:
        print(WRONG_VALUES)


if __name__ == '__main__':
    main()
