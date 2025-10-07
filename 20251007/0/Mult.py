from fractions import Fraction
from decimal import Decimal

def multiplier(x, y, Type):
    return Type(x)*Type(y)

print(multiplier("1.6", "2.3", Decimal))

