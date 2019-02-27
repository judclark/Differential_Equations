## Runge Kutta Method (RK4) for solving first order differential equations ##
## Returns approximation of y(interval_end) ##

import math

## Equation in form of f(t,y)
## EX: y-t**2+1 , math.cos(t)+2*y , 2-math.exp(-4*t)-2*y

equation = 'y-t**2+1'
init_t = 0
init_y = 0.5
interval_end = 2
step_size = 0.2


def Runge_Kutta(equation, t, y, interval_end, h):
    while(round(t,10) < interval_end):
        k1 = h * eval(equation)
        t = t + h/2
        y = y + (k1)/2
        k2 = h * eval(equation)
        y = y - (k1)/2 + (k2)/2
        k3 = h * eval(equation)
        t = t + h/2
        y = y - (k2)/2 + k3
        k4 = h * eval(equation)
        y = y - k3
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6

    return y

if __name__ == '__main__':
    approx = Runge_Kutta(equation, init_t, init_y, interval_end, step_size)
    print(approx)
