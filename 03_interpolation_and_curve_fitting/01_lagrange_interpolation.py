'''
Method: Lagrange Interpolation
Section: Interpolation and Curve Fitting
''' 
x = [0, 20, 40, 60, 80, 100]
y = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]
m = len(x) #function returns number of list elements
n = m-1
xp = float(input('Enter x : '))
yp = 0 #initialization of summation variable
for i in range(n+1):
    L = 1 #initialization of product variable
    for j in range(n+1):
        if j != i: #condition to perform product
            L *= (xp - x[j])/(x[i] - x[j])  #product of x terms
    yp += y[i]*L
print('For x = %.1f, y = %.1f' % (xp,yp))
