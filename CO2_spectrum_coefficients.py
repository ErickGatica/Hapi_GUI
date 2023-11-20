#Absorption coefficients
from hapi import *
import matplotlib.pyplot as plt

#To calculate an absorption coefficient
#-> absorptionCoefficient_HT
#-> absorptionCoefficient_Voigt
#-> absorptionCoefficient_Lorentz
#-> absorptionCoefficient_Doppler
#-> absorptionCoefficient_SDVoigt
#-> absorptionCoefficient_Galatry

#Review options in manual, for instace path length for default is 1m

#Getting data for CO2 in the range of 2000-2100cm^-1

fetch('CO2',2,1,2000,2400)

#Pressure and temperature for coeffcient in atm and K
P=2;
T=1000;

# Lets go with absorption coefficient
nu,coef=absorptionCoefficient_Lorentz(SourceTables='CO2',Diluent={'air':1.0},Environment={'T':300.,'p':1.2})

# Lets go with absorption Spectrum
nu,absorp=absorptionSpectrum(nu,coef);

# Lets go with transmittance Spectrum
nu,trans=transmittanceSpectrum(nu,coef);

# Lets go with radiance Spectrum
nu,radi = radianceSpectrum(nu,coef);

# Set the font to resemble LaTeX
#plt.rcParams['text.usetex'] = True
#plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

# Creating the Figure 1 coefficient
fig1, ax1 = plt.subplots()
# Creating the plot
ax1.plot(nu,coef)
# Add a legend
ax1.legend(loc='upper right')
# Label the axes
ax1.set_xlabel(r'$\nu$')
ax1.set_ylabel(r'Coefficient $cm^2/molecule$')
# Title
ax1.set_title('Absorption coefficient for $^{12}C^{16}O_2$ $T$='+str(T)+'K $P$='+str(P)+'atm')

# Creating the Figure 2 absorption spectrum
fig2, ax2 = plt.subplots()
# Creating the plot
ax2.plot(nu,absorp)
# Add a legend
ax2.legend(loc='upper right')
# Label the axes
ax2.set_xlabel(r'$\nu$')
ax2.set_ylabel(r'Absorbance')
# Title
ax2.set_title('Absorption spectrum for $^{12}C^{16}O_2$ $T$='+str(T)+'K $P$='+str(P)+'atm')

# Creating the Figure 3 transmittance spectrum
fig3, ax3 = plt.subplots()
# Creating the plot
ax3.plot(nu,trans)
# Add a legend
ax3.legend(loc='upper right')
# Label the axes
ax3.set_xlabel(r'$\nu$')
ax3.set_ylabel(r'Coefficient $cm^2/molecule$')
# Title
ax3.set_title('Transmittance spectrum for $^{12}C^{16}O_2$ $T$='+str(T)+'K $P$='+str(P)+'atm')

# Creating the Figure 4 radiance spectrum
fig4, ax4 = plt.subplots()
# Creating the plot
ax4.plot(nu,radi)
# Add a legend
ax4.legend(loc='upper right')
# Label the axes
ax4.set_xlabel(r'$\nu$')
ax4.set_ylabel(r'Coefficient $cm^2/molecule$')
# Title
ax4.set_title('Radiance spectrum for $^{12}C^{16}O_2$ $T$='+str(T)+'K $P$='+str(P)+'atm')







#Showing the plot
plt.show()





