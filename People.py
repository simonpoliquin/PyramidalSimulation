# this class is the basic for the represantion of a person
import random



class People(object):

    conversionCoefficient = 0 #probability of being converted can take value between 0 and 1
    averageValueConversionCoefficient = 0 #average value taken by the coefficient
    standardDeviationConversionCoefficient = 0  # standard deviation of the coefficient

    leavingCoefficient = 0 #probability of leaving can take value between 0 and 1
    averageValueLeavingCoefficient = 0  #average value taken by the coefficient
    standardDeviationLeavingCoefficient = 0  # sandard deviation of the coefficient

    isConverted = False ;
    hasBeenConverted = False;
    CanBeenConverted = True;





    def __init_(self):
        self.conversionCoefficient =0
        self.leavingCoefficient =0




    def makePeople(self,averageValueConversionCoefficient, standardDeviationConversionCoefficient , averageValueLeavingCoefficient , standardDeviationLeavingCoefficient):

        self.conversionCoefficient = self.conversionCoefficientGenerator(averageValueConversionCoefficient,standardDeviationConversionCoefficient)
       # print(self.conversionCoefficient)






    def conversionCoefficientGenerator(self,averageValueConversionCoefficient,standardDeviationConversionCoefficient ):

        coefficient =  random.normalvariate(averageValueConversionCoefficient,standardDeviationConversionCoefficient)
        coefficient =  self.ReturnValueBetweenZeroAndOne(coefficient)
        return coefficient



 #    def leavingCoefficientGenerator(self,leavingCoefficient,standardDeviationLeavingCoefficient):


    def ReturnValueBetweenZeroAndOne(self,coefficient):

        if coefficient < 0:
            return 0

        if coefficient > 1:
            return 1
        else:
            return coefficient


    def Conversion(self):
        randomValue =random.randint(0,100)
        # if the random integer is smaller than coefficient the person is converted
        if randomValue <= (self.conversionCoefficient * 100): # multiply by 100 for obtening a value between 0 and 100
            self.isConverted = True
            self.hasBeenConverted = True
            self.canBeenConverted = False
        else:
            self.isConverted = False
            self.hasBeenConverted = True
            self.canBeenConverted = False

    def Leaving(self):
        randomValue =random.randint(0,100)
        # if the random integer is smaller than coefficient the person is converted
        if randomValue <= (self.leavingCoefficient* 100): # multiply by 100 for obtening a value between 0 and 100
            self.isConverted = False
            self.hasBeenConverte = True;
            self.canBeenConverted = False;







