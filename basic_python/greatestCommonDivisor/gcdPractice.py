def gcd(num_1, num_2):

    while num_1 % num_2 != 0:
        old_num_1 = num_1
        old_num_2 = num_2

        num_1 = num_2
        num_2 = old_num_1 % old_num_2
    
    return num_2

class Fraction:

    def __init__(self, top, bottom):
        self.numerator = top
        self.denomenator = bottom

    def __str__(self):

        return(str(self.numerator) + "/" + str(self.denomenator)) 

    def __add__(self, other_function):
        new_numerator = self.numerator * other_function.denomenator + other_function.numerator * self.denomenator
        new_denomenator = self.denomenator * other_function.denomenator
        greatest_common_divisor = gcd(new_numerator, new_denomenator)

        return Fraction(new_numerator // greatest_common_divisor, new_denomenator // greatest_common_divisor)

    def __equal__(self, other_function):
        first_number = self.numerator * other_function.denomenator
        second_number = self.denomenator * other_function.numerator

        return first_number == second_number

x = Fraction(1, 3)
y = Fraction(1, 4)
print(x + y)
print(x == y)