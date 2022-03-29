# import numpy as np
import matplotlib.pyplot as plt
import math

# FUNCTIONS TO GET SLOPE, INTERCEPT AND R-SQUARE VALUES

# SUM(x)
def sum_list(num_1):
    sum = 0
    for i in range(len(num_1)):
        sum = sum + num_1[i]
    # print (sum)
    return (sum)


# SUM(x^2) by x values

def sum_list_square(num_1):
    sum = 0
    for i in range(len(num_1)):
        sum = sum + (num_1[i] * num_1[i])
    # print (sum)
    return (sum)


# SUM of (xy)
def sum_pdt(num_1, num_2):
    pdt = 0
    list_xy = []
    for i in range(len(num_1)):
        list_xy.append(num_1[i] * num_2[i])
    for j in range(len(list_xy)):
        pdt = pdt + (list_xy[j])
    # print (pdt)
    return (pdt)


# Slope
def slope(num_1, num_2):
    s_nu = (len(num_1) * (sum_pdt(num_1, num_2))) - (sum_list(num_1) * (sum_list(num_2)))
    s_de = (len(num_1) * (sum_list_square(num_1))) - (sum_list(num_1) * (sum_list(num_1)))
    slope = s_nu / s_de
    return (slope)


# Intercept
def intercept(num_1, num_2):
    i_nu = ((sum_list(num_2)) * (sum_list_square(num_1)) - (sum_list(num_1)) * (sum_pdt(num_1, num_2)))
    i_de = (len(num_1) * (sum_list_square(num_1))) - (sum_list(num_1) * (sum_list(num_1)))
    incpt = i_nu / i_de
    return (incpt)


# R-square value
def rsquare(num_1, num_2):
    r_nu = (len(num_1) * (sum_pdt(num_1, num_2))) - (sum_list(num_1) * (sum_list(num_2)))
    g = (((len(num_1)) * (sum_list_square(num_1))) - ((sum_list(num_1)) * (sum_list(num_1)))) \
        * (((len(num_1)) * (sum_list_square(num_2))) - ((sum_list(num_2)) * (sum_list(num_2))))
    r_de = math.sqrt(g)
    r = r_nu / r_de
    rsq = r * r
    return (rsq)
