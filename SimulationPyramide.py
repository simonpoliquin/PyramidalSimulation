from People import *

ni = 1 # number of conversion minimum by turn
NumberOfPeopleConverted = 0
NumberOfConversion = NumberOfPeopleConverted + ni # equation of the number of people  w
NumberOfPeople = 100 # Number ofr the people in the simulation

averageValueConversionCoefficient = 0.5  # average value taken by the coefficient
standardDeviationConversionCoefficient = 0.2  # standard deviation of the coefficient

averageValueLeavingCoefficient = 0.5  # average value taken by the coefficient
standardDeviationLeavingCoefficient = 0.2  # sandard deviation of the coefficient


peopleUntouched = [People() for i in range(NumberOfPeople)]
for people in peopleUntouched:
    people.makePeople(averageValueConversionCoefficient, standardDeviationConversionCoefficient ,averageValueLeavingCoefficient ,standardDeviationLeavingCoefficient)

