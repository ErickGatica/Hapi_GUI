from hapi import *
import matplotlib.pyplot as plt

#Starting the local database in folder 'data'
db_begin('data')
molecule='H2O';
#Downloading the data
fetch(molecule,1,1,500,14000)

#Getting Stick data
x,y=getStickXY('H2O');

# Calculating to plot difference between
# Voigt and Lorentzian lineshape
wmin=3002;#wavenumber of interest
wmax=3008;#wavenumber of interest
w0=3005;#unperturbed line position
wn=arange(wmin,wmax,0.01);
voi=PROFILE_VOIGT(w0,0.1,0.3,0,wn); #Voigt
lor=PROFILE_LORENTZ(w0,0.3,0,wn); #Lorentz

#For using latex font
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

#Subplots
fig1, ax1 = plt.subplots()
ax1.plot(x,y)
ax1.legend(loc='upper right')
ax1.set_xlabel(r'$cm^{-1}$')
ax1.set_ylabel(r'$cm/molecule$')
ax1.set_title('Stick plot '+molecule)

# Lets do a zoom in 4020;4035
numinzoom=4020;
numaxzoom=4035;
#Subplot
fig2, ax2 = plt.subplots()
ax2.plot(x,y);
ax2.legend(loc='upper right')
ax2.set_xlabel(r'$\nu$')
ax2.set_ylabel(r'Coefficient $cm^2/molecule$')
ax2.set_title('Stick Plot for '+molecule)
ax2.set_xlim(numinzoom, numaxzoom)

## Voigt and lorentzian plot
diff_v_l=voi-lor;
fig3, (ax3, ax4) = plt.subplots(2, 1)
ax3.plot(wn,voi,'red'); #plotting both
ax3.plot(wn,lor,'blue');

ax4.plot(wn,diff_v_l);
#Showing plots
plt.show()
