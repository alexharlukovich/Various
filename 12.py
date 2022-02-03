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

number = float(input("Input your positive number: "))
sum = ((number)*(number + 1)) / 2

print("The sum of the first", number, "positive numbers is ", sum)

#task 8 Souvenirs and trinkets Compound interest

souvenir = float(input("How many souvenirs do you want to byu?: "))
trinket = float(input("How many trinkets do you want to byu?: "))

s = 75.33
t = 112.61

mass = souvenir * s + trinket * t

print("Your order has weight of %.2f" % mass, "gramms")

#task 9 Compound interest

d = float(input("Input your deposite: "))
pr = 0.04
interest1 = d * ((1+(pr/12*100))**1)
interest2 = d * ((1+(pr/12*100))**2)
interest3 = d * ((1+(pr/12*100))**3)

print("Your money sum at the first year will be %.2f, after second year will be %.2f, after third year will be %.2f" % (interest1, interest2, interest3))

#task 10 Arithmetic
from math import log10
a = int(input("input the 'a' number: "))
b = int(input("input the 'b' number: "))
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a * b)
print(a, "/", b, "=", a / b)
print(a, "%", b, "=", a % b)
print("decimal logarithm of", a,  "=", log10(a))
print(a, "the extent of", b, "=", a**b)

# task 11 fuel consumption

us = float(input("Input fuel consumption in MPG: "))

lpg = 3.785
kmpm = 1.609

lpk = (100 * lpg) / (us * kmpm)
print("Your fuel consumption in Canada will be %.2f" % lpk, "l/100km")

#task 12 Distance between points on the Earth