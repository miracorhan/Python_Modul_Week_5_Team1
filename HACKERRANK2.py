import math

class Complex(object):
    # Initialize the real and imaginary parts of the complex number
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overload the addition operator
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    # Overload the subtraction operator
    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return Complex(real, imaginary)

    # Overload the multiplication operator
    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    # Overload the division operator
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2  # Denominator for division
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real, imaginary)

    # Method to calculate the modulus of a complex number
    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)  # |z| = sqrt(a^2 + b^2)
        return Complex(real, 0)  # Return as a complex number with 0 imaginary part

        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')