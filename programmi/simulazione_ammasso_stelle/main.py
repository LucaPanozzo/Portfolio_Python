import matplotlib.pyplot as plt
import numpy as np

sigma = 5.          #km/s
a = 5.              #pc
M = 10000.          #M_Sun
x = []
y = []
r_list = []
v_list = []
M_list = []

def M_r(r):

    return M*(r/a)**3*(1+(r/a)**2)**(-3/2)

def cluster():

    for i in range(10000):

        A = np.random.rand()
        B = np.random.rand()

        phi = 2*np.pi*A
        r = np.sqrt(a**2/(B**(-2/3)-1))
        
        r_list.append(r)

        x.append(r*np.cos(phi))
        y.append(r*np.sin(phi))

        m = np.sqrt(-2*sigma**2*np.log(1-A))*np.cos(2*np.pi*B)
        n = np.sqrt(-2*sigma**2*np.log(1-A))*np.sin(2*np.pi*B)

        v_list.append(np.sqrt(m**2+n**2))
        M_list.append(M_r(r)/M)

    plt.subplot(2,2,1)
    plt.hist(r_list, bins = 50, range = (0,20), density = "True", color = "white", edgecolor = "cyan")
    plt.xlabel("r [pc]")
    plt.ylabel("PDF")
    plt.grid()

    plt.subplot(2,2,2)
    plt.hist(v_list, bins = 50, range = (0,25), density = "True", color = "white", edgecolor = "green")
    plt.xlabel("v [km/s]")
    plt.ylabel("PDF")
    plt.grid()

    plt.subplot(2,2,3)
    plt.plot(r_list, M_list,"m.", markersize = 0.5)
    plt.xlabel("r [pc]")
    plt.xlim(0,20)
    plt.ylabel("M(r)/M")
    plt.text(0.77,0.83,"M = $10^{4} M_{\odot}$")
    plt.grid()

    plt.subplot(2,2,4)
    plt.plot(x,y,"r.",markersize = 0.75)
    plt.xlim(-20,20)    
    plt.ylim(-20,20)
    plt.xlabel("x [pc]")
    plt.ylabel("y [pc]")
    plt.grid()

    plt.tight_layout()
    plt.show()

    return

cluster()
