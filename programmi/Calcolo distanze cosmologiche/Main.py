import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np

comoving=[]
luminosity = []
redshift=[]
backtime = []

H_0 = 67.2                                  #km/s/Mpc                                                                  
c = 299272.458                              #km/s                                                              
Omega_M = 0.2726
Omega_L = 0.7274
convert=1e5/3.086e24*3.1536e7*1e9           #to transform H_0 in Gyr

m = c/H_0                                   #Mpc
n = H_0*convert                             #Gyr

def plots():

    z = float(input("Enter the value of the redshift z:"))

    while(z>=0):
    
        integrand = lambda x: 1/np.sqrt(((1+x)**3)*Omega_M + Omega_L)
        integral_time = lambda x: 1/((1+x)*np.sqrt((Omega_M*(1+x)**3.+Omega_L)))

        Distance = integrate.quad(integrand , 0.0 , z)
        Timepast = integrate.quad(integral_time, 0.0, z)

        Dist = Distance[0]
        Time = Timepast[0]
    
        Dc = Dist * m
        Dl = Dc * (1+z)
        T = Time / n

        comoving.append(Dc)
        luminosity.append(Dl)
        backtime.append(T)
        redshift.append(z)

        z = z-0.1

    plt.subplot(1,2,1)
    plt.plot(redshift,comoving, 'g-', label='Comoving', linewidth=0.75)
    plt.plot(redshift,luminosity, 'c-', label='Luminosity', linewidth=0.75)
    plt.legend()
    plt.xlabel('Redshift z')
    plt.ylabel('Distance [Mpc]')
    plt.title("Distances")
    plt.grid()

    plt.subplot(1,2,2)
    plt.plot(redshift,backtime, 'm-', linewidth=0.75) 
    plt.xlabel('Redshift z')
    plt.ylabel('Time [Gyr]')
    plt.title("Lookback Time")
    plt.grid()
    
    plt.tight_layout()
    plt.show()

    return

plots()
