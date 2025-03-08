# Number 1- Euler Method
def euler_method(f, t0, y0, h, n):
    t = t0
    y = y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def function(t, y):
    return t - y**2

t0 = 0
y0 = 1
h = 0.2
n = 10

result = euler_method(function, t0, y0, h, n)
print(result)

# Number 2- Runge-Kutta 
def runge_kutta(f, t0, y0, h, n):
    t = t0
    y = y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)

        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y

def function(t, y):
    return t - y ** 2

t0 = 0
y0 = 1
h = 0.2
n = 10

result = runge_kutta(function, t0, y0, h, n)
print(result)
