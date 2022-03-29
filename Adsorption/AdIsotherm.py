import math
import Notes_StatPlot as np
import matplotlib.pyplot as plt
import admod

# EFFECT OF CONCENTRATION


ph = float(input("Enter the pH of the solution, pH: "))  # pH of the solution
mass = float(input("Enter the adsorbent dose in grams, m: "))  # mass or dose of the adsorbent(g)
temp = float(input("Enter the temperature in Kelvin, T: "))  # temperature of the reaction in K
list_n = []
list_ci = []
list_ce = []  # ce - equilibrium concentration
list_re = []  # re - removal efficiency
list_qe = []
list_logce = []
list_lnce = []
list_logqe = []
list_cebyqe = []
list_log_cebyqe = []


def concentration():

    b_wavelength = float(input("Enter the wavelength before adsorption: "))
    a_wavelength = float(input("Enter the wavelength after adsorption: "))
    ce = round((a_wavelength / b_wavelength) * ci, 4)  # ce-Equilibrium concentration (Ce),
    cr = round(ci - ce, 4)  # concentration removed
    qe = round((cr / mass), 4)  # qe-quantity removed
    re = round((((ci - ce) / ci) * 100), 4)  # Removal efficiency
    logce = round(math.log(ce, 10), 4)  # Freundlich: x-axis 'logce'
    logqe = round(math.log(qe, 10), 4)  # Freundlich: y-axis 'logqe'
    cebyqe = round(ce / qe, 4)  # Langmuir: x-axis 'ce', y-axis 'ce/qe'
    log_cebyqe = round(math.log(cebyqe, 10), 4)  # Redlich-Peterson: y-axis 'log(ce/qe)'
    lnce = round(math.log(ce), 4)  # Tempkin: x-axis 'lnce'

    '''print(ce)
    print(re)
    print(logce)
    print(qe)
    print(logqe)
    print(cebyqe)
    print(log_cebyqe)'''

    list_ce.append(ce)
    list_re.append(re)
    list_qe.append(qe)
    list_logce.append(logce)
    list_logqe.append(logqe)
    list_cebyqe.append(cebyqe)
    list_log_cebyqe.append(log_cebyqe)
    list_lnce.append(lnce)


print("Enter 0 to EXIT")
ci = 1
n = 0  # Serial number, n
while ci > 0:
    ci = float(input("Enter the initial concentration of the solution in mg/L: "))
    list_ci.append(ci)
    if ci > 0:
        concentration()
        n = n + 1
        list_n.append(n)
    else:
        exit

'''print(list_ce)
print(list_re)
print(list_qe)
print(list_logce)
print(list_logqe)
print(list_cebyqe)
print(list_log_cebyqe)
print(list_lnce)'''

# ISOTHERM TABLE: Data for Freundlich, Langmuir, Redlich-Peterson & Tempkin
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")
print("ISOTHERM MODEL:" + "\t\t\t" + "pH:", ph, "\t\t\t" + "Temperature:", temp, "K", "\t\t\t" + "Adsorbent Dose:",
      mass, "mg/L")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")
print(
    "S.No" + "\t" + "Ci(mg/L)" + "\t" + "%Removal" + "\t" + "Ce(mg/L)" + "\t" + "Qe(mg/g)" + "\t" + "Ce/Qe" + "\t\t" + "log(Ce)" + "\t\t" + "log(Qe)" + "\t\t" + "log(Ce/Qe)" + "\t" + "ln(Ce)")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")
x = 0
for x in range(n):
    print("%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (
    list_n[x], list_ci[x], list_re[x], list_ce[x], list_qe[x], list_cebyqe[x], \
    list_logce[x], list_logqe[x], list_log_cebyqe[x], list_lnce[x]))
    n = n + 1
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")

# Freundlich result
freu_slop = round(admod.slope(list_logce, list_logqe), 3)
freu_incpt = round(admod.intercept(list_logce, list_logqe), 3)
freu_rsqr = round(admod.rsquare(list_logce, list_logqe), 3)

# Langmuir result
lang_slop = round(admod.slope(list_ce, list_cebyqe), 3)
lang_incpt = round(admod.intercept(list_ce, list_cebyqe), 3)
lang_rsqr = round(admod.rsquare(list_ce, list_cebyqe), 3)

# Tempkin result
tpkn_slop = round(admod.slope(list_lnce, list_qe), 3)
tpkn_incpt = round(admod.intercept(list_lnce, list_qe), 3)
tpkn_rsqr = round(admod.rsquare(list_lnce, list_qe), 3)

# Redlich-Peterson result
rp_slop = round(admod.slope(list_logce, list_log_cebyqe), 3)
rp_incpt = round(admod.intercept(list_logce, list_log_cebyqe), 3)
rp_rsqr = round(admod.rsquare(list_logce, list_log_cebyqe), 3)

# ISOTHERM TABLE: RESULT for Freundlich, Langmuir, Redlich-Peterson & Tempkin
print("----------------------------------------------------------------------------")
print("ISOTHERM MODEL:" + "\t\t" + "SLOPE" + "\t\t" + "INTERCEPT" + "\t\t" + "R-SQUARE")
print("----------------------------------------------------------------------------")
x = 0
for x in range(4):
    if x == 0:
        print("FREUNDLICH" + "\t\t" + "%s\t\t%s\t\t\t%s" % (freu_slop, freu_incpt, freu_rsqr))
        n = n + 1
    if x == 1:
        print("LANGMUIR" + "\t\t" + "%s\t\t%s\t\t\t%s" % (lang_slop, lang_incpt, lang_rsqr))
        n = n + 1
    if x == 2:
        print("TEMPKIN" + "\t\t\t" + "%s\t\t%s\t\t\t%s" % (tpkn_slop, tpkn_incpt, tpkn_rsqr))
        n = n + 1
    if x == 3:
        print("REDLICH-PETERSON" + "\t" + "%s\t\t%s\t\t\t%s" % (rp_slop, rp_incpt, rp_rsqr))
        n = n + 1
print("----------------------------------------------------------------------------")


# PLOT

def plot(x, y):
    plt.plot(x, y, marker='o', linestyle="")
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(pTitle)
    plt.show()


for tr in range(4):
    if tr == 0:
        pTitle = "Freundlich Model"
        xLabel = "log Ce"
        yLabel = "log Qe"
        plot(list_logce, list_logqe)  # calling for Freundlich plot
    tr = tr + 1
    if tr == 1:
        pTitle = "Langmuir Model"
        xLabel = "Ce(mg/L)"
        yLabel = "Ce/Qe"
        plot(list_ce, list_cebyqe)  # calling for Langmuir plot
    tr = tr + 1
    if tr == 2:
        pTitle = "Tempkin Model"
        xLabel = "ln Ce"
        yLabel = "Qe(mg/g)"
        plot(list_logce, list_log_cebyqe)  # calling for Redlich-peterson plot
    tr = tr + 1
    if tr == 3:
        pTitle = "Redlich-Peterson Model"
        xLabel = "log Ce"
        yLabel = "log Ce/Qe"
        plot(list_lnce, list_qe)  # calling for Tempkin plot
    tr = tr + 1

print("           ================  THANK YOU ALL  ===============")





