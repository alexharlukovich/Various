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

# from math import sqrt
#
# GRAVITY = 9.8
#
# d = float(input("Object release height, m:  "))
#
# vf = sqrt(2 * GRAVITY * d)
# print("The object will reach the ground at speed %.1f" % vf, "m/s")

# task 20 The equation of state of an ideal gas

# PV = nRT,
# где P – это давление в паскалях, V – объем в литрах, n – количество ве-
# щества в молях, R – универсальная газовая постоянная, равная 8,314
# Дж/(моль·К), а T – температура по шкале Кельвина.
# Напишите программу для измерения количества

# P = float(input("Input pressure: "))
# R = 8.314
# n = float(input("Input volume: "))
# V = 12
# T = float(input("Input temperature Kelvins: "))
#
# n = (P * V) / (R * T)
# print(n)

# task 21 The area of the triangle
# h = float(input("Input the height of the triangle, m: "))
# b = float(input("Input the length of the triangle base, m: "))
#
# area = (b * h) / 2
#
# print("The area of your triangle is %.2f meters" % area)

# task 22 The area of the triangle (another one)

# s1 = float(input("Input lenght of the first side of the triangle, m : "))
# s2 = float(input("Input lenght of the second side of the triangle, m : "))
# s3 = float(input("Input lenght of the third side of the triangle, m : "))
#
# s = (s1 + s2 + s3) / 2
# area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
#
# print("The area of your triangle is %.2f meters" % area)

# task 23 The area of the regular polygon
# from math import tan, pi
#
# s = float(input("Enter the lenght of the sides, m: "))
# n = int(input("Enter the number of the sides, pcs: "))
#
# area = (n * s ** 2) / (4 * tan(pi / n))
#
# print("The area of the pokygon is ", area)

#task 24 Time units

# SEC_PER_DAY = 86400
# SEC_PER_HOUR = 3600
# SEC_PER_MINUTE = 60
#
# d = int(input("Enter number of days: "))
# h = int(input("Enter number of hours: "))
# m = int(input("Enter number of minutes: "))
#
# total = d * SEC_PER_DAY + h * SEC_PER_HOUR + m * SEC_PER_MINUTE
#
# print("Your number of seconds is", total)

# task 25 Time units (another one)

# SEC_PER_DAY = 86400
# SEC_PER_HOUR = 3600
# SEC_PER_MINUTE = 60
#
# seconds = int(input("Enter number of seconds: "))
#
# days = seconds / SEC_PER_DAY
# seconds = seconds % SEC_PER_DAY
# hours = seconds / SEC_PER_HOUR
# seconds = seconds % SEC_PER_HOUR
# minutes = seconds / SEC_PER_MINUTE
# seconds = seconds % SEC_PER_MINUTE
#
# print("Duration:", \
# "%d:%02d:%02d:%02d." % (days, hours, minutes, seconds))

#task 26 Current time

# from time import asctime
#
# a = asctime()
# print(a)

# task 27 When is Easter?
# from math import floor
#
# year = int(input("Enter the year you're interested in: "))
#
# a = year / 19
# b = floor(year / 100)
# c = year % 100
# d = floor(b / 4)
# e = b % 4
# f = floor((b + 8) / 25)
# g = floor((b - f - 1) / 3)
# h = (19 * a + b - d - g + 15) % 30
# i = floor(c / 4)
# k = c % 4
# l = (32 + 2 * e + 2 * i - h - k) % 7
# m = floor((a + 11 * h + 22 * l) / 451)
# month = int(h + l + 7 * m + 114) / 31
# day = int(1 + (h + l - 7 * m +114) % 31)
# print("Easter in year ", year, "will be at %.0f %.0f" % (day, month))

# task 28 Body Mass Index

# weight = float(input("Enter your weight, kilo: "))
# height = float(input("Enter your height, cm: "))
#
# bmi = weight / (height ** 2)
#
# print("Your body mass index is %.2f" % bmi)

# task 29 Temperature taking into account wind

# WC_OFFSET = 13.12
# WC_FACTOR1 = 0.6215
# WC_FACTOR2 = -11.37
# WC_FACTOR3 = 0.3965
# WC_EXPONENT = 0.16
#
# temp = float(input("Temperature, Celsius degrees: "))
# speed = float(input("Wind speed, km/h: "))
#
# wci = WC_OFFSET + \
# WC_FACTOR1 * temp + \
# WC_FACTOR2 * speed ** WC_EXPONENT + \
# WC_FACTOR3 * temp * speed ** WC_EXPONENT
# print("Коэффициент охлаждения ветром равен", round(wci))

# task 30 Pressure units
#
# kpa = float(input("Enter your value in kPa: "))
# psi = kpa / 6.895
#
# print("Your value in psi is %.2f" % psi)

# task 31 Celsius to Fahrenheit and Kelvin

# the same as task 30

# task 32 The sum of digits in a number

# a = int(input("Your number, please: "))
# b = a % 10
# c = a // 10 % 10
# d = a // 100 % 10
# e = a // 1000
# print(b + c + d + e)

# task 33 Sorting three numbers

# a = int(input("Number 1: "))
# b = int(input("Number 2: "))
# c = int(input("Number 3: "))
#
# nmax = max(a, b, c)
# nmin = min(a, b, c)
# medium = a + b + c - nmax - nmin
# print("Числа в порядке возрастания:")
# print(" ", nmin)
# print(" ", medium)
# print(" ", nmax)

# task 34 Yesterday's bread

# BREAD_PRICE = 3.49
# DISCOUNT_RATE = 0.60
#
# num_loaves = int(input("Enter number of yesterday's loaves: "))
# regular_price = num_loaves * BREAD_PRICE
# discount = regular_price * DISCOUNT_RATE
# total = regular_price - discount
#
# print("Nominal price: %5.2f" % regular_price)
# print("Discount: %5.2f" % discount)
# print("Total: %5.2f" % total)

# task 35 Odd or even?

# num = int(input("Enter your number: "))
#
# if num == 1:
#     print(num, "even")
# else:
#     print(num, 'odd')

# task 36 Canine age

# num = int(input("Enter your age: "))
# if 0<= num <=2:
#     print("Your canine age is:", 21)
# elif num >= 2:
#     num1 = 21 + num * 4 - 2
#     print("Your canine age is:", num1)
# elif num < 0:
#     print("Wrong number!")

# task 37 Vowels and consonants

# letter = input("Enter letter of the latin alphabet: ")
# if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#     print("it's vowel letter")
# elif letter == "y":
#     print("Sometimes this letter is vowel, sometimes is consonant")
# else:
#     print("This letter is consonant")

# task 38 Guess the figure

# nsides = int(input("Enter number the sides of the shape: "))
# name = ""
# if nsides == 3:
#     name = "triangle"
# elif nsides == 4:
#     name = "rectangle"
# elif nsides == 5:
#     name = "pentagon"
# elif nsides == 6:
#     name = "hexagon"
# elif nsides == 7:
#     name = "heptagon"
# elif nsides == 8:
#     name = "octagon"
# elif nsides == 9:
#     name = "nonagon"
# elif nsides == 10:
#     name = "decagon"
# if name == "":
#     print("The entered number of sides is not supported by the program.")
# else:
#     print("This figure is:", name)

# task 39 How many days in the month?

# month = input("Enter the name of the month:")
# days = 31
# if month == "Apil" or month == "June" or month == "September" or month == "November":
#     days = 30
# elif month == "February":
#     days = "28 or 29"
# print("Number of the days in your month is:", days)
from calendar import monthrange
import datetime

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "December"]
month_number = months.index( input("Enter the name of the month:") )
print("Number of the days in your month is:", monthrange(datetime.datetime.now().year, month_number)[1])

# task 40 Sound volume

vol = int(input("Enter the sound volume: "))

if vol == 130:
    print("Jackhammer")
elif vol == 106:
    print("Petrol lawn mower")
elif vol == 70:
    print("Alarm clock")
elif vol == 40:
    print("Quiet room")
elif 130 <= vol <= 106:
    print("Loud sound, my boy! Between jackhammeh and petrol lawn mower")
elif 70 <= vol <= 106:
    print("Loud sound! Between petrol lawn mower and alarm clock")
elif 40 <= vol <= 70:
    print("Quiet sound! Between alarm clock and quiet room!")
else:
    print("Hey! Sound volume beyond measurement!")