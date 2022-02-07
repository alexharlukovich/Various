import math
import random
y = float(99)
z = math.sqrt(y)

print(z)

import random

w = []
for i in range(0, 999):
    w.append(i)
print(random.choice(w))

# # requesting name + surname
# # first = input("Your name is: ")
# # last = input("Your surname is: ")
# # both = first  +"  "+ last
# #
# # # print(both)
# #
# # num_chars = len(first)
# # # print("Your name contains ", num_chars, " symbols")
# # initials = first[0] + last[0]
# # print("Your initials is ", initials)
#
#
# # task 1 Post adress
#
# print("Boris Yeltsin")
# print("President of Russia")
# print("Kremlin, 14-868, Moscow, Red Square")
# print("Likes drink wodka a lot")
#
# # task 2 Greeting
#
# name = input("Your name, please: ")
# print("Nice to see you,", name, ", my dear friend")
#
# # task 3 room area
#
# # requesting the measures of the room
#
# length = float(input("Input the room's length: "))
# width = float(input("Input the room's widht: "))
#
# # calculate the area of the room
#
# area = length * width
#
# # let's display the result
#
# print("Room's square is ", area, "square meters.")
#
# # task 4 The area of the garden plot
#
# # requesting the measures of the room
# lenght1 = float(input("Input the garden plot length(foots): "))
# width1 = float(input("Input the garden plot width(foots): "))
#
# # square feet per acre
# sqft_per_acre = 43560
#
# # calculating area of the garden plot
# plot_area = (lenght1 * width1) / sqft_per_acre
#
# # let's display the result
# print("Area of the garden plot is  %.2f." % plot_area, "acres!")

#task 5  bottles deposite

# less_depostie = 0.15
# more_deposite = 0.35
#
# less = int(input("How many small bottles do you have: "))
# more = int(input("How many big bottles do you have: "))
#
# summ = less * less_depostie + more * more_deposite
#
# print("Yours profit from the bottles revenue $%.2f." % summ)

# task 6 taxes and tips


# tax_rate = 0.05
# tip_rate = 0.18
#
# cost = float(input("Enter the bill amount: "))
#
# tax = cost * tax_rate
# tip = cost * tip_rate
# total = cost + tax + tip
#
# print("Налог составил %.2f, чаевые – %.2f, общая сумма заказа: %.2f" % (tax, tip, total))
#
# print("The tax was: %.2f, tips: %.2f, total \
# ammount: %.2f" % (tax, tip, total))

#task 7 The sum of the first n positive numbers

# number = float(input("Input your positive number: "))
# sum = ((number)*(number + 1)) / 2
#
# print("The sum of the first", number, "positive numbers is ", sum)
#
# #task 8 Souvenirs and trinkets Compound interest
#
# souvenir = float(input("How many souvenirs do you want to byu?: "))
# trinket = float(input("How many trinkets do you want to byu?: "))
#
# s = 75.33
# t = 112.61
#
# mass = souvenir * s + trinket * t
#
# print("Your order has weight of %.2f" % mass, "gramms")
#
# #task 9 Compound interest
#
# d = float(input("Input your deposite: "))
# pr = 0.04
# interest1 = d * ((1+(pr/12*100))**1)
# interest2 = d * ((1+(pr/12*100))**2)
# interest3 = d * ((1+(pr/12*100))**3)
#
# print("Your money sum at the first year will be %.2f, after second year will be %.2f, after third year will be %.2f" % (interest1, interest2, interest3))
#
# #task 10 Arithmetic
# from math import log10
# a = int(input("input the 'a' number: "))
# b = int(input("input the 'b' number: "))
# print(a, "+", b, "=", a + b)
# print(a, "-", b, "=", a * b)
# print(a, "/", b, "=", a / b)
# print(a, "%", b, "=", a % b)
# print("decimal logarithm of", a,  "=", log10(a))
# print(a, "the extent of", b, "=", a**b)
#
# # task 11 fuel consumption
#
# us = float(input("Input fuel consumption in MPG: "))
#
# lpg = 3.785
# kmpm = 1.609
#
# lpk = (100 * lpg) / (us * kmpm)
# print("Your fuel consumption in Canada will be %.2f" % lpk, "l/100km")
#
# #task 12 Distance between points on the Earth
# from math import radians
#
# cor1 = float(input("input point 1: "))
# cor2 = float(input("input point 2: "))
# cor3 = float(input("input point 3: "))
# cor4 = float(input("input point 4: "))
#
# #distance = 6371,01 x arccos(sin(t1) x sin(t2) + cos(t1) x cos(t2) x cos(g1 - g2)).
#
# distance = 6371.01 * ((radians(cor1) * radians(cor2)) + (radians(cor1) * radians(cor2) * radians(cor3 - cor4)))
# print(distance)

# task 13 Change of banknotes

# cents_per_toonie = 200
# cents_per_loonie = 100
# cents_per_quarter = 25
# cents_per_dime = 10
# cents_per_nickel = 5
#
# cents = int(input("Input the amount to be exchanged: "))
# print(cents // cents_per_toonie, "двухдолларовых монет")
# cents = cents % cents_per_toonie
# print(cents // cents_per_loonie, "однодолларовых монет")
# cents = cents % cents_per_loonie
# print(cents // cents_per_quarter, "четвертьдолларовых монет")
# cents = cents % cents_per_quarter
# print(cents // cents_per_dime, "десятицентовых монет")
# cents = cents % cents_per_dime
# print(cents // cents_per_nickel, "пятицентовых монет")
# cents = cents % cents_per_nickel
#
# print(" ", cents, "центов")


# task 14 Height

# foot = 12
# cm_inch = 2.54
#
# print("Input your height:")
# feet = int(input("Введите количество футов: "))
# inchs = int(input("Введите количество дюймов: "))
# cm = (feet * foot + inchs) * cm_inch
# print("Your height in cm is ", cm)

# task 15 Distance

# Для этого упражнения вам необходимо будет написать программу, кото-
# рая будет запрашивать у пользователя расстояние в футах. После этого
# она должна будет пересчитать это число в дюймы, ярды и мили и вывести
# на экран. Коэффициенты для пересчета единиц вы без труда найдете
# в интернете.

# IN_PER_FT = 12
# FT_PER_YARD = 3
# ML_PER_FOOT = 5280
#
# print("Input your distance in feet:")
# feet_ = int(input("Your distance is: "))
# yard = feet_ * FT_PER_YARD
# mile = feet_ / ML_PER_FOOT
# inches = feet_ * IN_PER_FT
# print("Your trip is %.2f yards, %.2f miles, %.2f inches" % (yard, mile, inches))
#
# # task 16 Area and volume
#
# from math import pi
#
# r = radius = float(input("Input your circle radius: "))
# area = pi * r ** 2
# volume = 4 / 3 * (pi * r ** 3)
#
# print(" Your circle area is %.2f cm, you sphere volume is %.2f cm" % (area, volume))

# task 17 Heat capacity

# WATER_HEAT_CAPACITY = 4.0186
# ELECTRICITY_PRICE = 8.9
# J_TO_KWH = 2.777e-7
#
# volume = float(input("Volume of water in ml: "))
# d_temp = float(input("Temperature rise(in Celsius degrees): "))
#
# q = volume * d_temp * WATER_HEAT_CAPACITY
# kwh = q * J_TO_KWH
# cost = kwh * ELECTRICITY_PRICE
# print("Needs %.2f joules of energy" % q)
# print("The cost of energy %.2f cents: " % cost)

# task 18 Cylinder volume

# from math import pi
#
# r = radius = float(input("Input your cylinder radius: "))
# h = height = float(input("Input your cylinder height: "))
#
# v = pi * r * h
#
# print("Your cylinder's volume is %.1f" % v, "cm3")

# task 19 Free fall

from math import sqrt

GRAVITY = 9.8

d = float(input("Object release height, m:  "))

vf = sqrt(2 * GRAVITY * d)
print("The object will reach the ground at speed %.1f" % vf, "m/s")

# task 20 The equation of state of an ideal gas

# PV = nRT,
# где P – это давление в паскалях, V – объем в литрах, n – количество ве-
# щества в молях, R – универсальная газовая постоянная, равная 8,314
# Дж/(моль·К), а T – температура по шкале Кельвина.
# Напишите программу для измерения количества

P = float(input("Input pressure: "))
R = 8.314
n = float(input("Input volume: "))
V = 12
T = float(input("Input temperature Kelvins: "))

n = (P * V) / (R * T)
print(n)