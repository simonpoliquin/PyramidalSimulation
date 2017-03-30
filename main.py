import random
from People import *

averageValueConversionCoefficient = 0.5  # average value taken by the coefficient
standardDeviationConversionCoefficient = 0.2  # standard deviation of the coefficient

averageValueLeavingCoefficient = 0.5  # average value taken by the coefficient
standardDeviationLeavingCoefficient = 0.2  # sandard deviation of the coefficient


person.makePeople(averageValueConversionCoefficient, standardDeviationConversionCoefficient ,averageValueLeavingCoefficient ,standardDeviationLeavingCoefficient)
print(person.conversionCoefficient)


person.Conversion()

print(person.hasBeenConverted)
print(person.isConverted)
print(person.canBeenConverted)
