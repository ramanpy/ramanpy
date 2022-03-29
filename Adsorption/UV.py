import matplotlib.pyplot as plt
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

def uv():
    file = pd.ExcelFile('uv.xlsx')
    df = file.parse('data')

    wavelength = df['Wavelength'].values                # Wavelength value
    percent_transmittance = df['%T'].values             # Percentage transmittance values
    transmittance = percent_transmittance/100           # Transmittance values
    length = float(input('Enter the cell length (cm): '))
    log_inv_T = np.log10(1/transmittance)               # Absorbance
    alpha = (2.303) * (log_inv_T/length)
    energy = 1242/wavelength                            # Energy in ev
    sq_alpha_energy = np.square(alpha * energy)
    sq_root_alpha_energy = np.sqrt(alpha * energy)
    #print(wavelength)
    #print(percent_transmittance)
    #print(transmittance)
    #print(alpha)

    #print(energy)
    #print(sq_root_alpha_energy)
    #plot(wavelength,percent_transmittance)
    #plot(energy, sq_alpha_energy)
    #plot(energy, sq_root_alpha_energy)


    # OPTICAL CONDUCTIVITY
    refractive_index = (1/percent_transmittance) + np.sqrt(1/(percent_transmittance-1))
    optical_conductivity = (alpha*refractive_index*299792458)/(4*3.14)
    print(optical_conductivity)
    plot(wavelength, optical_conductivity)

uv()

