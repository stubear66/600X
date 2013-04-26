# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#    

def runTrial(n, numViruses, maxPop, 
             maxBirthProb, clearProb, resistances, mutProb):
    additionalSteps = 150
    virusList = []
    for i in range(numViruses):
        virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = TreatedPatient(virusList, maxPop)
    totalSteps = n + additionalSteps
    for step in range(totalSteps):
       if step == n:
           p.addPrescription('guttagonol')
       pop = p.update()
    
    return pop

def drawHist(results, numTrials):
    yLabel = "Number of Trials"
    xLabel = "Number of Viruses"
    sp = [221,222,223,224]
    i = 0
    for n in sorted (results):
        print n
        pylab.subplot(sp[i])
        popList = results[n]
        pylab.title("Add drug at step " + str(n))
        pylab.hist(popList, 20)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        i += 1
        

    
    pylab.show()      
    
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    #Initialization
    #delayList = [300, 150, 75, 0]
    delayList = [150]
    #Patient init variables
    numViruses = 100
    maxPop = 1000
    #Virus init variables
    maxBirthProb = 0.1
    clearProb = 0.05
    #clearProb = 0.10
    resistances = { 'guttagonol': True }
    mutProb = 0.005
    
    results = {}
    
    for n in delayList:
        cured = 0
        popList = []
        for i in range(numTrials):
            pop = runTrial(n, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb)
            popList.append(pop)
            if pop == 0:
                cured +=1
        results[n] = popList
        #print popList
        print "Delay : %(delay)d Percentage cured %(percent)2f" % {"delay" : n, "percent" : cured/float(numTrials) }
        

    drawHist(results, numTrials)   
    





#
# PROBLEM 2
#

def runTrialTwoDrugs (n, numViruses, maxPop, 
                      maxBirthProb, clearProb, resistances, mutProb):
    additionalSteps = 150
    virusList = []
    for i in range(numViruses):
        virusList.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    p = TreatedPatient(virusList, maxPop)
    totalSteps = n + (additionalSteps * 2)
    for step in range(totalSteps):
       if step == additionalSteps:
           #print "Adding guttagonol at step %(step)d" % {'step' : step}
           p.addPrescription('guttagonol')
       if step == (n + additionalSteps):
            #print "Adding grimpex at step %(step)d" % {'step': step}
            p.addPrescription('grimpex')  
       pop = p.update()
    
    return pop
    
    
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    #Initialization
    delayList = [300, 150, 75, 0]
    #delayList = [150]
    #Patient init variables
    numViruses = 100
    maxPop = 1000
    #Virus init variables
    maxBirthProb = 0.1
    clearProb = 0.05
    #clearProb = 0.10
    resistances = { 'guttagonol': False, 'grimpex' : False }
    #mutProb = 0.005
    mutProb = 0.010
    
    results = {}
    
    for n in delayList:
        cured = 0
        popList = []
        print "Running trials for delay %(delay)d" % {'delay' : n}
        for i in range(numTrials):
            #print "Trial: " + str(i)
            pop = runTrialTwoDrugs(n, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb)
            popList.append(pop)
            if pop < 50:
                cured +=1
        results[n] = popList
        #print popList
        print "Delay : %(delay)d Percentage cured %(percent)2f" % {"delay" : n, "percent" : cured/float(numTrials) }
        

    drawHist(results, numTrials)   
