import numpy as np
import matplotlib.pyplot as plt
from math import *
from ru_local import *

#Alina

#Aigerim


#Liza

def number5():
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

def number8():
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

def number9():
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

def main():
    number = input(INPUTING)
    try:
        number = int(number)
        if int(number) == 5:
            number5()
        elif int(number) == 8:
            number8()
        elif int(number) == 9:
            number9()
        else:
            print(SORRY)
    except ValueError:
        print(WRONG_VALUES)

if __name__ == '__main__':
    main()