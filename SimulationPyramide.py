from People import *
from collections import deque
import math


class PyramidalSimulation(object):


    ni = 10  # number of conversion minimum by turn
    NumberOfPeopleConverted = 0
    NumberOfPeople = 1000000  # Number ofr the people in the simulation

    NumberOfCycle = 100

    averageValueConversionCoefficient = 0.5  # average value taken by the coefficient
    standardDeviationConversionCoefficient = 0.2  # standard deviation of the coefficient

    averageValueLeavingCoefficient = 0.5  # average value taken by the coefficient
    standardDeviationLeavingCoefficient = 0.2  # sandard deviation of the coefficient

    lossCoefficient = 0.1
    ConversionCoefficient = 0.5


    peopleUntouched = deque()

    peopleConverted = deque()
    peopleNotConverted = deque()


    def __init_(self):
        [self.peopleUntouched.append(People()) for i in range(self.NumberOfPeople)] #Create the list with the people
        for people in self.peopleUntouched: #Initialise the person in the list
            people.makePeople(self.averageValueConversionCoefficient, self.standardDeviationConversionCoefficient,
                              self.averageValueLeavingCoefficient, self.standardDeviationLeavingCoefficient)

    def Conversion(self):

        NumberOfConversionAttempt = self.NumberOfConversion()
        for j in range(0, NumberOfConversionAttempt):
            self.peopleUntouched[0].Conversion() # Attemp to Conversion
            self.PlaceInGoodList(self.peopleUntouched[0]) #following the result place the person in the good list
            self.peopleUntouched.popleft() # remove the person from the list of person untouched.


    def PlaceInGoodList(self,people):
        if self.people.isConverted:
            people.append(self.peopleUntouched[0])
        else:
            people.append(self.peopleUntouched[0])



    def NumberOfConversion(self):


        self.numberOfPeopleConverted = len(self.peopleConverted) # Number of people in the list equal the number of people in the pyramdial scheme

        numberOfConversion = math.floor(self.ConversionCoefficient*self.NumberOfPeopleConverted) + self.ni # number of maximal conversion attempt.
        NumberOfPeopleLeftToConverted = len(self.peopleUntouched)
        if numberOfConversion > NumberOfPeopleLeftToConverted:
            return NumberOfPeopleLeftToConverted #  There is less people to converte than the number of people making a attempt
        else:
            return numberOfConversion # standar case follow the equation above

    def Leaving(self):
        NumberOfLeavingAttempt = self.NumberOfLeaving()
        for j in range(0, NumberOfLeavingAttempt):
            self.peopleConverted[0].Conversion() # Attemp to Conversion
            self.PlaceInGoodList(self.peopleConverted[0]) #following the result place the person in the good list
            self.peopleConverted.popleft() # remove the person from the list of person untouched.

    def NumberOfLeaving(self):

        self.numberOfPeopleConverted = len(self.peopleConverted) # Number of people in the list equal the number of people in the pyramdial scheme

        numberOfPeopleLeaving = math.floor(self.lossCoefficient * self.NumberOfPeopleConverted) + self.ni # number of maximal people thinking leaving

        if numberOfPeopleLeaving > self.numberOfPeopleConverted :
            return self.numberOfPeopleConverted #  There is less people who can leave than the number of people converted
        else:
            return numberOfPeopleLeaving # standar case follow the equation above


    def PymarimalSimulation(self):
        for i in range (0,self.NumberOfCycle):
            self.Conversion()
            self.Leaving()










