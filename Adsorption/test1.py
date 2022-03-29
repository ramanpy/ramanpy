
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


def Kinetics():
    file = pd.ExcelFile('sample.xlsx')
    df1 = file.parse('Kinetics')

    time = df1['Time'].values
    b_max = df1['λmax(B)'].values  # b_max is the value before Adsorption
    a_max = df1['λmax(A)'].values  # a_max is the value after Adsorption
    b_max = b_max[0]
    list_time = []
    list_amax = []
    #print(time)
    #print(a_max)
    #print(b_max)
    #print(type(b_max))
    #ph = float(input("Enter the pH of the solution, pH: "))                             # pH of the solution
    #mass = float(input("Enter the adsorbent dose in grams, m: "))                       # mass or dose of the adsorbent(g)
    #temp = float(input("Enter the temperature in Kelvin, T: "))                         # temperature of the reaction in K
    i = 0
    while (a_max[i]!=a_max[i+1]):
        list_time.append(time[i])
        list_amax.append(a_max[i])
        i = i + 1
    list_time.append(time[i])
    list_amax.append(a_max[i])
    time = np.array(list_time)
    a_max = np.array(list_amax)

    '''
    print(time)
    print(a_max)
    '''

    ph = float(input("Enter the pH of the solution, pH: "))  # pH of the solution
    mass = float(input("Enter the adsorbent dose in grams, m: "))  # mass or dose of the adsorbent(g)
    temp = float(input("Enter the Temperature in K: "))  # mass or dose of the adsorbent(g)
    ci = float(input("Enter the initial concentration of the solution in mg/L, c: "))   # concentration of the solution in mg/L
    #b_max = float(input("Enter the absorption value before adsorption, λmax(B): "))     # b_max is the value after Adsorption
    rem_eff = np.around((((b_max - a_max) / b_max) * 100),4)    # Removal efficiency
    ce = ((a_max/b_max)*ci)                          # ce-Equilibrium concentration (Ce)
    cr = (ci - ce)                                   # concentration removed
    qe = (cr / mass)                                 # qe-quantity removed
    logqe = np.log10(qe)
    qe_qt = (qe[-1]-qe)

    logqe_qt = []
    i = 0
    while qe_qt[i] != 0:
        c = math.log10(qe_qt[i])
        logqe_qt.append(format(c,'.3f'))
        i += 1
    for i in range(len(time)):
        if len(logqe_qt)!=len(time):
            logqe_qt.append('inf')

    tbyqt = (time/qe)
    log_t = np.log10(time)
    ln_t = np.log(time)
    root_t = np.sqrt(time)

    '''
    print(rem_eff)
    print(ce)
    print(cr)
    print(qe)
    print(logqe)

    print(qe_qt)
    print(logqe_qt)
    print(tbyqt)
    print(log_t)
    print(ln_t)
    print(root_t) '''


    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(format("KINETICS MODEL:",'<16') +format("pH:",'>8'), ph, "" + format("Temperature:",'>16'), temp, "K"  + format("Adsorbent Dose:",'>18'),
          mass, "mg/L" + format("Conc.:",'>12'), ci, "mg/L"  + format("λmax(B):",'>12'), b_max)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(
        "S.No" + format("time(min)",'>12') + format("%Removal",'>12') + format("Ce(mg/L)",'>12') + format("Qe(mg/g)",'>12') +format("log(Qe-Qt)",'>15') + format("log(Qe)",'>12') +format("t/Qt",'>10') +format("log t",'>12') +format("ln t",'>10') +format("sq.root t",'>16'))
    print("----------------------------------------------------------------------------------------------------------------------------------")

    x = 0
    for x in range(len(qe_qt)):
        print("%s%s%s%s%s%s%s%s%s%s%s" % (
            format((x + 1), '^4'), format(time[x], '>9'), format(format(rem_eff[x], ".3f"), '>14'),
            format(format(ce[x], ".3f"), '>12'), format(format(qe[x], ".3f"), '>12'),
            format(logqe_qt[x], '>14'),
            format(format(logqe[x], ".3f"), '>13'), format(format(tbyqt[x], ".3f"), '>12'),
            format(format(log_t[x], ".3f"), '>12'), format(format(ln_t[x], ".3f"), '>10'),
            format(format(root_t[x], ".3f"), '>15')))
        x = x + 1
    print("----------------------------------------------------------------------------------------------------------------------------------")

Kinetics()