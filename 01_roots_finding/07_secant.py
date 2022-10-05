'''
Method: Secant
''' 

from math import cos

def secant(fn,x1,x2 = 0,tol = 0.000001,maxiter = 100):
    for iteration in range(maxiter):
        xnew = x2 - (x2-x1)/(fn(x2)-fn(x1)) * fn(x2)
        if abs(xnew - x2) < tol : break
        else:
            x1 = x2
            x2 = xnew
    else:
        print("Warning: Maximum number of iterations is reached!")
    return xnew, iteration


f = lambda x: x**2 - 2              # Example 1
#f = lambda x: x**2 + cos(x)**2 - 4*x   # Example 2 

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

r,n = secant(f,x1,x2,0.001,10)

print("Root = %f at %d iterations"%(r,n))

           
