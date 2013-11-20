class Polynomial:
    def __init__(self, init_coeff):
        self.coefficients = init_coeff

    def __call__(self, x):
        result = 0.0
        for i, a in enumerate(self.coefficients):
            result += a*x**i
        return result

    def differentiate(self):
        new_coefficients = []
        for i, a in enumerate(self.coefficients):
            new_coefficients.append(i*a)
        del new_coefficients[0]
        self.coefficients = new_coefficients

