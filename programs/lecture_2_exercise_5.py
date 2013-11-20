from pylab import plot, show, legend
from random import normalvariate


T = 200
alphas = [ 0, 0.8, 0.9 ]

for alpha in alphas:
    x_series = []
    x_series.append(0)
    for i in range(T):
        x_value = alpha*x_series[i] + normalvariate(0,1)
        x_series.append(x_value)
    plot(x_series, label="alpha = " + str(alpha) )

legend()
show()

