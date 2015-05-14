from StdSuites.Type_Names_Suite import machine_location

# __author__ = 'wanli'
__author__ = 'Wanli xue'

# import math
#
# def PrintN(n):
#     if n==1:
#         print n
#     elif n>1:
#         PrintN(n-1)
#         print n
#     return
#
# def sum(n):
#     sum = 0
#     for num in range(1,n+1,1):
#         sum += (sum+1000)*(1+0.047)
#         # print num
#     return sum

# print (-math.sqrt(10)-2)/2

# help(format)

# weight = float(raw_input('type ur weight\n'))
# height = float(raw_input('type ur height\n'))
# # help(format)
#
# print("{:.2f}".format(weight/(height**2)))

# pi= 3.14
# radius = float(raw_input('radius is '))
# area = pi*radius**2
# print area , '\a'
# print(1)


# input = float(raw_input())
#
# hour = (int)(input/3600)
# minutes = (int)((input%3600)/60)
# sec = (int)(input%60)
#
# print hour, minutes, sec
#
#
# a = (int)(raw_input())
# b = (int)(raw_input())
# c = (int)(raw_input())
#
# tem = (float)(c**2 -b**2 - a**2)/(2*a*b)
#
# d = math.degrees(math.acos(tem))
# print("{:.1f}".format(d))
#
#
#
#
#
# print 'Hello\nWorld'

# print sum(10)


import math

a = (float)(raw_input())
b = (float)(raw_input())
c = (float)(raw_input())

# print math.pow(2,2)
tem = (float)(-c**2 +b**2 + a**2)/(2*a*b)

d = math.degrees(math.acos(tem))
print("{:.1f}".format(d))