import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sb
import pandas as pd
# EFFECT OF ISOTHERM

def IsothermResult(x,y):
    reg = np.polyfit(x,y, deg=1)  # out: array(slope, intercept)

    # r_square
    correlation_mat = np.corrcoef(x,y)
    r = correlation_mat[0,1]
    Isorsquare = format(r**2,".3f")
    IsoSlope = format(reg[0],".3f")
    IsoIntercept = format(reg[1],".3f")
    return([IsoSlope,IsoIntercept,Isorsquare])


def KineticsResult(x,y):
    reg = np.polyfit(x,y, deg=1)  # out: array(slope, intercept)

    # r_square
    correlation_mat = np.corrcoef(x,y)
    r = correlation_mat[0,1]
    KinSquare = format(r**2,".3f")
    KinSlope = format(reg[0],".3f")
    KinIntercept = format(reg[1],".3f")
    return([KinSlope,KinIntercept,KinSquare])

def ThermoResult(x,y):
    reg = np.polyfit(x,y, deg=1)  # out: array(slope, intercept)

    # r_square
    correlation_mat = np.corrcoef(x, y)
    r = correlation_mat[0, 1]
    ThermoSquare = format(r ** 2, ".3f")
    ThermoSlope = format(reg[0], ".3f")
    ThermoIntercept = format(reg[1], ".3f")
    return ([ThermoSlope, ThermoIntercept, ThermoSquare])


# Linear regression plot
def plot(x,y):
    reg = np.polyfit(x,y, deg=1)  # out: array(slope, intercept)
    trend = np.polyval(reg, x)
    plt.scatter(x, y)
    plt.plot(x, trend, 'r')
    plt.show()

# EFFECT OF CONCENTRATION

def Isotherms():
    file = pd.ExcelFile('sample.xlsx')
    df1 = file.parse('Isotherms')

    ci = df1['Ci(mg/L)'].values     # ci is initial concentration of dye
    b_max = df1['λmax(B)'].values   # b_max is the value before Adsorption
    a_max = df1['λmax(A)'].values   # a_max is the value after Adsorption

    '''list = []
    print(ci)
    print(b_max)
    print(a_max)'''

    ph = float(input("Enter the pH of the solution, pH: "))         # pH of the solution
    m = float(input("Enter the adsorbent dose in grams, m: "))      # mass or dose of the adsorbent(g)
    temp = float(input("Enter the temperature in Kelvin, T: "))     # temperature of the reaction in K

    ce = (a_max / b_max) * ci         # ce-Equilibrium concentration (Ce),
    cr = ci - ce                      # concentration removed
    qe = (cr / m)                     # qe-quantity removed
    re = (((ci - ce) / ci) * 100)     # Removal efficiency
    logce = np.log10(ce)              # Freundlich: x-axis 'logce'
    logqe = np.log10(qe)              # Freundlich: y-axis 'logqe'
    cebyqe = (ce / qe)                # Langmuir: x-axis 'ce', y-axis 'ce/qe'
    log_cebyqe = np.log10(cebyqe)     # Redlich-Peterson: y-axis 'log(ce/qe)'
    lnce = np.log(ce)                 # Tempkin: x-axis 'lnce'

    '''print(ce)
    print(re)
    print(logce)
    print(qe)
    print(logqe)
    print(cebyqe)
    print(log_cebyqe)
    print(lnce)'''

    # ISOTHERM TABLE: Data for Freundlich, Langmuir, Redlich-Peterson & Tempkin
    print("----------------------------------------------------------------------------------------------------------------")
    print(format("ISOTHERM MODEL:" ,'<16') + format("pH:",'>8'), ph,"" + format("Temperature:",'>16'), temp, "K" + format("Adsorbent Dose:",'>26'), m,"mg/L")
    print("----------------------------------------------------------------------------------------------------------------")
    print(
        "S.No" + format("Ci(mg/L)",'>11') + format("%Removal",'>12') +format("Ce(mg/L)",'>12')+ format("Qe(mg/g)",'>12') +format("Ce/Qe",'>12') + format("log(Ce)",'>12') +format("log(Qe)" ,'>12')+format("log(Ce/Qe)",'>12') +format("ln(Ce)",'>12'))
    print("----------------------------------------------------------------------------------------------------------------")
    x = 0
    for x in range(len(ce)):
        print("%s%s%s%s%s%s%s%s%s%s" % (
            format((x + 1),'^4'), format(ci[x],'>10'), format(format(re[x],".3f"),'>12'), format(format(ce[x],".3f"),'>12'), format(format(qe[x],".3f"),'>12'), format(format(cebyqe[x],".3f"),'>12'),
            format(format(logce[x],".3f"),'>12'), format(format(logqe[x],".3f"),'>12'), format(format(log_cebyqe[x],".3f"),'>12'), format(format(lnce[x],".3f"),'>12')))
    print("----------------------------------------------------------------------------------------------------------------")


    # ISOTHERM RESULTS: Freundlich, Langmuir, Redlich-Peterson & Tempkin

    print("--------------------------------------------------------")
    print(format("ISOTHERM MODEL:",'<18') + format("SLOPE",'>12') + format("INTERCEPT",'>14') + format("R-SQUARE",'>12'))
    print("--------------------------------------------------------")
    x = 0
    if x == 0:
        result = IsothermResult(logce, logqe)
        print(format("FREUNDLICH",'<18') + "%s%s%s" % (format(result[0],'>12'), format(result[1],'>12'), format(result[2],'>12')))
        x = x + 1
    if x == 1:
        result = IsothermResult(ce, cebyqe)
        print(format("LANGMUIR",'<18') + "%s%s%s" % (format(result[0],'>12'), format(result[1],'>12'), format(result[2],'>12')))
        x = x + 1
    if x == 2:
        result = IsothermResult(lnce, qe)
        print(format("TEMPKIN",'<18') +"%s%s%s" % (format(result[0],'>12'), format(result[1],'>12'), format(result[2],'>12')))
        x = x + 1
    if x == 3:
        result = IsothermResult(logce, log_cebyqe)
        print(format("REDLICH-PETERSON",'<18') + "%s%s%s" % (format(result[0],'>12'), format(result[1],'>12'), format(result[2],'>12')))
    print("--------------------------------------------------------")

#Isotherm plots

    for i in range(4):
        if i==0:
            dict = {"TITLE": 'FREUNDLICH ISOTHERM PLOT', "XLABLE": 'log Ce', "YLABLE": 'log Qe'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(logce, logqe)
        if i==1:
            dict = {"TITLE": 'LANGMUIR ISOTHERM PLOT', "XLABLE": 'Ce', "YLABLE": 'log Ce/Qe'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(ce, cebyqe)
        if i==2:
            dict = {"TITLE": 'TEMPKIN ISOTHERM PLOT', "XLABLE": 'ln Ce', "YLABLE": 'Qe'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(lnce, qe)
        if i==3:
            dict = {"TITLE": 'REDLICH-PETERSON ISOTHERM PLOT', "XLABLE": 'log Ce', "YLABLE": 'log Ce/Qe'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(logce, log_cebyqe)


# EFFECT OF TIME
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


    # KINETICS TABLE: RESULT for Legargren, Second order, Elovich & IPD
    i = 0
    time_1 = time[:-1]
    qe_qt_1 = qe_qt[:-1]
    '''while (qe_qt[i] != 0):
        time_1 = np.append(time_1,time[i])
        qe_qt_1 = np.append(qe_qt_1,qe_qt[i])
        i = i + 1'''
    logqe_qt_1 = np.log10(qe_qt_1)

    print("-----------------------------------------------------------------")
    print(format("KINETICS MODEL:",'<25') +format("SLOPE",'>8') +format("INTERCEPT",'>16') + format("R-SQUARE",'>16'))
    print("-----------------------------------------------------------------")
    x = 0
    if x == 0:
        #print(time_1)
        #print(qe_qt_1)
        #print(logqe_qt_1)
        result = KineticsResult(time_1,logqe_qt_1)
        print(format("LEGARGREN FIRST ORDER","<25") + "%s%s%s" % (format(result[0],">8"), format(result[1],">14"), format(result[2],">16")))
        x = x + 1

    if x == 1:
        result = IsothermResult(time, tbyqt)
        print(format("PSEUDO SECOND ORDER","<25") + "%s%s%s" % (format(result[0],">8"), format(result[1],">14"), format(result[2],">16")))
        x = x + 1
    if x == 2:
        result = IsothermResult(log_t,qe)
        print(format("ELOVICH KINETICS","<25") + "%s%s%s" % (format(result[0],">8"), format(result[1],">14"), format(result[2],">16")))
        x = x + 1
    if x == 3:
        result = IsothermResult(root_t, qe)
        print(format("INTRA PARTICLE DIFFUSION","<25") + "%s%s%s" % (format(result[0],">8"), format(result[1],">14"), format(result[2],">16")))
    print("-----------------------------------------------------------------")


    # Isotherm plots
    for i in range(4):
        if i == 0:
            dict = {"TITLE": 'LEGARGREN PSEUDO FIRST ORDER PLOT', "XLABLE": 'Time', "YLABLE": 'log Qe-Qt'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(time_1, logqe_qt_1)
        if i == 1:
            dict = {"TITLE": 'PSEUDO SECOND ORDER PLOT', "XLABLE": 'Time', "YLABLE": 't/Qt'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(time, tbyqt)
        if i == 2:
            dict = {"TITLE": 'ELOVICH KINETICS PLOT', "XLABLE": 'ln t', "YLABLE": 'Qt'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(ln_t, qe)
        if i == 3:
            dict = {"TITLE": 'INTRA-PARTICLE DIFFUSION PLOT', "XLABLE": 'Square root(t)', "YLABLE": 'Qt'}
            plt.title(dict['TITLE'], fontsize=14)
            #plt.legend('LEGEND', fontsize=12)
            plt.xlabel(dict['XLABLE'], fontsize=12)
            plt.ylabel(dict['YLABLE'], fontsize=12)
            plot(root_t, qe)


# EFFECT OF TEMPERATURE (THERMODYNAMICS)

def Thermodynamics():
    file = pd.ExcelFile('sample.xlsx')
    df1 = file.parse('Thermodynamics')

    temp = df1['Temp(K)'].values   # Temperature in Kelvin
    b_max = df1['λmax(B)'].values  # b_max is the value before Adsorption
    a_max = df1['λmax(A)'].values  # a_max is the value after Adsorption
    #print(temp)
    #print(b_max)
    #print(a_max)

    ph = float(input("Enter the pH of the solution, pH: "))  # pH of the solution
    m = float(input("Enter the adsorbent dose in grams, m: "))  # mass or dose of the adsorbent(g) per 1000 mL of solution
    ci = float(input("Enter the initial concentration of the solution in mg/L, c: "))  # concentration of the solution in mg/L
    #b_max = float(input("Enter the absorption value before adsorption, λmax(B): "))  # b_max is the value after Adsorption
    rem_eff = np.around((((b_max - a_max) / b_max) * 100), 4)  # Removal efficiency
    ce = ((a_max / b_max) * ci)  # ce-Equilibrium concentration (Ce)
    cr = ci - ce  # concentration removed
    qe = (cr / m)  # qe-quantity removed
    re = (((ci - ce) / ci) * 100)   # Removal efficiency
    inv_temp = 1/temp               # inverse of temperature (X-axis)
    lnqembyce = np.log((qe/ce)*m)   # Y-axis
    delta_g_k = (-8.314 / 1000) * temp * lnqembyce  #  from K_L values, unit - kJ/K/mol

    '''print(qe)
    print(inv_temp)
    print(lnqembyce)
    #print(delta_g_k)
    print(type(qe))
    print(type(inv_temp))
    print(type(lnqembyce))'''

    result = ThermoResult(inv_temp, lnqembyce)
    #print(result)

    slop = float(result[0])
    incpt = float(result[1])

    '''print(slop)
    print(incpt)
    print(type(slop))
    print(type(incpt))'''

    delta_h = (-8.314 * slop)/1000              # unit - kJ/K/mol
    delta_s = (8.314 * incpt)/1000              # unit - kJ/K/mol
    delta_g = (delta_h - (temp * delta_s))      # unit - kJ/K/mol

    '''print(delta_h)
    print(delta_s)
    print(delta_g)'''

    delta_h1 = format(delta_h,".3f")
    delta_s1 = format(delta_s,".3f")
    delta_g1 = ["{:.3f}".format(x) for x in (delta_g)]

    '''print(slop)
    print(incpt)
    print(delta_h1)
    print(delta_s1)
    print(delta_g1)'''

    # THERMODYNAMICS RESULT
    print("------------------------------------")
    print("THERMODYNAMICS MODEL:")
    print("Concentration:",ci,"ppm  ", "pH:",ph)
    print("------------------------------------")
    print("    ∆H◦(kJ/K/mol):",delta_h1)
    print("    ∆S◦(kJ/K/mol):", delta_s1)
    print("------------------------------------")
    print(" Temperature(K)       ∆G◦(kJ/K/mol)")
    print("------------------------------------")
    for i in range (len(temp)):
        print("%s%s"%(format(temp[i],'>9'),format(delta_g1[i],'>22')))
    print("------------------------------------")

'''
    print("-------------------------------------------------------------------------------------")
    print("THERMODYNAMICS MODEL:"+ "\t\t\t" + "pH:", ph, "\t\t\t"+ "Concentration:",ci,"ppm" )
    print("-------------------------------------------------------------------------------------")
    print("       ∆H◦" + "\t\t\t\t" + "∆S◦" + "\t\t\t\t\t" + "∆G◦(kJ/K/mol)")
    print("   (kJ/K/mol)       (kJ/K/mol)     --------------------------------------------------")
    print("                                      303 K       313 K       323 K      333 K")
    print("-------------------------------------------------------------------------------------")
    print( "\t", delta_h1, "\t\t", delta_s1,"\t\t", delta_g1[0],"\t\t", delta_g1[1],"\t\t", delta_g1[2],"\t\t", delta_g1[3])
    print("-------------------------------------------------------------------------------------")
'''

#Isotherms()
#Kinetics()
#Thermodynamics()

# Starting point

def Option():
    print("-----SELECT THE DESIRED OPTION FROM THE FOLLOWING----")
    print(" 1- ISOTHERM   2-KINETICS    3-THERMODYNAMICS   0-EXIT")

a=1
while a!=0:
    try:
        print("WELCOME TO THE ADSORPTION WORLD")
        Option()
        a = int(input("Enter the desired option: "))
        if a >= 0 and a <= 4:
            if a == 1:
                Isotherms()
                print("Thank You.")

            if a == 2:
                Kinetics()
                print("Thank You.")

            if a == 3:
                Thermodynamics()
                print("Thank You.")

            if a == 0:
                print("THANK YOU.")
        else:
            print("ENTER THE CORRECT OPTION")
    except:
        print('ENTER THE INTEGER VALUE BETWEEN 0 TO 3')