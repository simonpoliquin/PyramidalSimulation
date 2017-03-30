from People import *
from collections import deque
ni = 10 # number of conversion minimum by turn
NumberOfPeopleConverted = 0
NumberOfConversion = NumberOfPeopleConverted + ni # equation of the number of people
NumberOfPeople = 1000000 # Number ofr the people in the simulation

NumberOfCycle = 100

averageValueConversionCoefficient = 0.5  # average value taken by the coefficient
standardDeviationConversionCoefficient = 0.2  # standard deviation of the coefficient

averageValueLeavingCoefficient = 0.5  # average value taken by the coefficient
standardDeviationLeavingCoefficient = 0.2  # sandard deviation of the coefficient

peopleUntouched = deque()
[peopleUntouched.append(People()) for i in range(NumberOfPeople)]
for people in peopleUntouched:
    people.makePeople(averageValueConversionCoefficient, standardDeviationConversionCoefficient ,averageValueLeavingCoefficient ,standardDeviationLeavingCoefficient)


peopleConverted = deque()
peopleNotConverted = deque()
for i in range (0,NumberOfCycle):
    for j in range (0,NumberOfConversion):
        peopleUntouched[0].Conversion()
        if  peopleUntouched[0].isConverted :
            peopleConverted.append(peopleUntouched[0])
        else:
            peopleNotConverted.append(peopleUntouched[0])
        peopleUntouched.popleft()

    NumberOfPeopleConverted = len(peopleConverted)
    print(NumberOfPeopleConverted)
    NumberOfConversion = NumberOfPeopleConverted + ni
    print('cycle:',i+1)








