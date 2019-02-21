import math

## equation in form of f(t,y)
## EX: y-t**2+1 , math.cos(t)+2*y , 2-math.exp(-4*t)-2*y

equation = 'math.cos(t)+2*y'
init_t = 0
init_y = 1
interval_end = 2
step_size = 0.1


def Euler(equation, t, y, interval_end, step_size):
    while(round(t,10) < interval_end):
        f = eval(equation)
        y = y + step_size * f
        t = t + step_size
    return y

if __name__ == '__main__':
    approx = Euler(equation, init_t, init_y, interval_end, step_size)
    print(approx)
