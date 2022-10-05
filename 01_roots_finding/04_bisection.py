'''
Method: Bisection
''' 
x1 = 0.5              
x2 = 1.4           
y1 = 2*x1**2-5*x1+3 
y2 = 2*x2**2-5*x2+3 

if y1*y2 > 0:       
    print('No roots exist within given interval')
    exit            

for i in range(1,101): 
    xh = (x1+x2)/2 
    yh = 2*xh**2-5*xh+3 
    y1 = 2*x1**2-5*x1+3 
    if abs(y1) < 1.0e-6: 
        break 
    elif y1*yh < 0: 
        x2 = xh 
    else: 
        x1 = xh 
print('The root: %.5f' % x1)
print('Number of bisections: %d' % i)
