import scipy.constants as c
import scipy.special as sp
import numpy as np

def energy_n(n):
    part1 = c.m_e/(2.0*(c.hbar**2))
    part2 = ((c.e**2)/(4.0*c.pi*c.epsilon_0))
    part3 = (-part1*part2**2)*(1.0/n**2)
    
    return round(part3/c.e,5)

#print energy_n(1)

def degToRad(deg):
    return round(deg * c.pi / 180.0,5)

def radToDeg(rad):
    return round(rad * 180.0 / c.pi,5)
    
def sphericalToCartesian(r,theta,phi):
    x = round(r * np.sin(theta) * np.cos(phi),5)
    y = round(r * np.sin(theta) * np.sin(phi),5)
    z = round(r * np.cos(theta),5)
    return x,y,z

#this guy is really weird. Can't seem to get Tutor's expected results
#without forcing it like this.
def cartesianToSpherical(x, y, z):
    r = round(np.sqrt(x**2 + y**2 + z**2),5)
    theta = round(np.arccos(z/(r)),5)
    phi = np.sqrt(x**2 + y**2)
    if phi == 0:
        phi = np.arctan(0)
    else:
        phi = round(np.arccos(x/(np.sqrt(x**2 + y**2))),5)   
    return r, theta, phi

#Taken from Week 5 Tutor        
def fact(n):
    if(n<=0):
        return 1
    return n*fact(n-1) 
        
#def assocLegendre(m,l):
#    #Assuming variable x is cos(theta) as given,
#    returnable = sp.lpmn(m,l,np.cos(1))
#    returnable[0][m][l] *= ((-1)**m)
#    return returnable[0][m][l]
#    
#print assocLegendre(2,2)  
#print np.cos(1)

def p00(theta):
  return 1

def p01(theta):
  return np.cos(theta)

def p02(theta):
  return 0.5*(3*np.cos(theta)**2-1)

def p03(theta):
  return 0.5*(5*np.cos(theta)**3-3*np.cos(theta))

def p11(theta):
  return np.sin(theta)

def p12(theta):
  return 3*np.sin(theta)*np.cos(theta)

def p13(theta):
  return 1.5*np.sin(theta)*(5*np.cos(theta)**2-1)

def p22(theta):
  return 3*np.sin(theta)**2

def p23(theta):
  return 15*np.sin(theta)**2*np.cos(theta)

def p33(theta):
  return 15*np.sin(theta)*(1-np.cos(theta)**2)

def assocLegendre(m,l):
  if m==0 and l==0:
    return p00
  elif m==0 and l==2:
    return p02
  elif m==1 and l==1:
    return p11
  elif m==3 and l==3:
    return p33
  elif m==0 and l==1:
    return p01
  elif m==2 and l==3:
    return p23
  elif m==2 and l==2:
    return p22
  elif m==1 and l==3:
    return p13
  elif m==1 and l==2:
    return p12
  elif m==0 and l==3:
    return p03
  else:
    return None
    
    
#f = assocLegendre(2,3)  
#print f(1)

def lag00(x):
  return 1
def lag01(x):  
  return np.poly1d([-1,1])(x)
def lag11(x):
  return np.poly1d([-2,4])(x)
def lag10(x):
  return 1
def lag02(x):
  return np.poly1d([1,-4,2])(x)
def lag12(x):
  return np.poly1d([3,-18,18])(x)
def lag22(x):
  return np.poly1d([12,-96,144])(x)
def lag21(x):
  return np.poly1d([-6,18])(x)
def lag20(x):
  return 2
def lag03(x):
  return np.poly1d([-1,9,-18,6])(x)
def lag13(x):
  return np.poly1d([-4,48,-144,96])(x)
def lag23(x):
  return np.poly1d([-20,300,-1200,1200])(x)
def lag33(x):
  return np.poly1d([-120,2160,-10800,14400])(x)
def lag32(x):
  return np.poly1d([60,-600,1200])(x)
def lag31(x):
  return np.poly1d([-24,96])(x)
def lag30(x):
  return 6


from scipy.special import laguerre

def assocLaguerre(p,qmp):
  if p == 0 and qmp == 0:
    return lag00
  elif p == 0 and qmp == 1:
    return lag01
  elif p == 1 and qmp == 1:
    return lag11
  elif p == 1 and qmp == 0:
    return lag10
  elif p == 0 and qmp == 2:
    return lag02
  elif p == 1 and qmp == 2:
    return lag12
  elif p == 2 and qmp == 2:
    return lag22
  elif p == 2 and qmp == 1:
    return lag21
  elif p == 2 and qmp == 0:
    return lag20
  elif p == 0 and qmp == 3:
    return lag03
  elif p == 1 and qmp == 3:
    return lag13
  elif p == 2 and qmp == 3:
    return lag23
  elif p == 3 and qmp == 3:
    return lag33
  elif p == 3 and qmp == 2:
    return lag32
  elif p == 3 and qmp == 1:
    return lag31
  elif p == 3 and qmp == 0:
    return lag30



def angular_wave_func(m,l,theta,phi):
    if m > 0:
        e = -1**m
    else:
        e = 1
    return np.round(e*np.sqrt(((1.0+2*l)*fact(l-abs(m)))/(4.0*c.pi*float(fact(l+abs(m)))))*np.exp((0+1j)*m*phi)*assocLegendre(m,l)(theta),5)

print angular_wave_func (0 ,0 ,0 ,0)


import scipy.constants as c
import numpy as np 

def radial_wave_func(n,l,r):
  a = c.physical_constants["Bohr radius"][0]
  na = n*a
  p1 = (2/na)**3
  p2 = fact(n-l-1)/(2*n*fact(n+l)**3.0)
  sqrt = np.sqrt(p1*p2)
  lag = assocLaguerre(2*l+1,n-l-1)((2*r)/na)
  pwr = np.exp(-r/na)*((2*r/na)**l)
  return np.round((sqrt*pwr*lag)/a**(-1.5),5)


#borrowed knowledge. this was hard
def hydrogen_wave_func(n, l, m, roa, Nx, Ny, Nz):
  a = c.physical_constants["Bohr radius"][0]
  plot = np.mgrid[-roa:roa:Nx*1j,-roa:roa:Ny*1j,-roa:roa:Nz*1j] #creates a 3D matrix containing all the points from -roa to roa, with the steps between each point determined by Nz,Ny or nx
  xx, yy, zz = [ np.swapaxes(plot[i],0,1) for i in xrange(3) ] #performs matrix transformations and transposes values for the axes
  rr, tt, pp = np.vectorize( cartesianToSpherical )( xx, yy, zz ) #passes all the arrays throug the cart to sphere func

  fullwave = angular_wave_func(m,l,tt,pp)*radial_wave_func(n,l,rr*a)

  mag = np.square( np.absolute( fullwave ) )  #psi square
  return np.round(xx,5), np.round(yy,5), np.round(zz,5), np.round(mag,5)
  

#11) propagation, rounding
#12) increase acc, inc comp time
#13) dec acc, no change comp time