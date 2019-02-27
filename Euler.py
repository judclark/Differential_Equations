## Euler Method for solving first order differential equations ##
## Returns approximation of y(interval_end) ##

import math

## equation in form of f(t,y)
## EX: y-t**2+1 , math.cos(t)+2*y , 2-math.exp(-4*t)-2*y

equation = 'math.cos(t)+2*y'
init_t = 0
init_y = 1
interval_end = 2
step_size = 0.1

def Euler(f, t, y, h, interval_end):
    while(round(t,10) < interval_end):
        f = eval(equation)
        y = y + h * f
        t = t + h
    return y

if __name__ == '__main__':
    approx = Euler(equation, init_t, init_y, step_size, interval_end)
    print(approx)
