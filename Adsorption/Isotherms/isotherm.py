import math
import Notes_StatPlot as np
import matplotlib.pyplot as plt

# EFFECT OF CONCENTRATION


ph = float(input("Enter the pH of the solution, pH: "))  # pH of the solution
m = float(input("Enter the adsorbent dose in grams, m: "))  # mass or dose of the adsorbent(g)
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
    x = []
    y = []
    b_wavelength = float(input("Enter the wavelength before adsorption: "))
    a_wavelength = float(input("Enter the wavelength after adsorption: "))
    ce = round((a_wavelength / b_wavelength) * ci, 4)  # ce-Equilibrium concentration (Ce),
    cr = round(ci - ce, 4)  # concentration removed
    qe = round((cr / m), 4)  # qe-quantity removed
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


def plot(x, y):
    plt.plot(x, y)
    plt.show()


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
print("ISOTHERM MODEL:" + "\t\t\t" + "pH:", ph, "\t\t\t" + "Temperature:", temp, "K", "\t\t\t" + "Adsorbent Dose:", m,
      "mg/L")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")
print(
    "S.No" + "\t" + "Ci(mg/L)" + "\t" + "%Removal" + "\t" + "Ce(mg/L)" + "\t" + "Qe(mg/g)" + "\t" + "Ce/Qe" + "\t\t" + "log(Ce)" + "\t\t" + "log(Qe)" + "\t\t" + "log(Ce/Qe)" + "\t" + "ln(Ce)")
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")
x = 0
for x in range(n):
    print("%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (
    list_n[x], list_ci[x], list_re[x], list_ce[x], list_qe[x], list_cebyqe[x], list_logce[x], list_logqe[x],
    list_log_cebyqe[x], list_lnce[x]))
    n = n + 1
print(
    "-------------------------------------------------------------------------------------------------------------------------------------------------")

# PLOT
plot(list_logce, list_logqe)  # calling for Freundlich plot
plot(list_ce, list_cebyqe)  # calling for Langmuir plot
plot(list_logce, list_log_cebyqe)  # calling for Redlich-peterson plot
plot(list_lnce, list_qe)  # calling for Tempkin plot

