import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # Your code here
    global CURRENTRABBITPOP, MAXRABBITPOP
    birthProb = 1 - (CURRENTRABBITPOP / float(MAXRABBITPOP) )
    r = random.random()
    if r < birthProb and CURRENTRABBITPOP < MAXRABBITPOP:
        CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # Your code here
    global CURRENTRABBITPOP, MAXRABBITPOP, CURRENTFOXPOP
    ate = False
    eatProb = CURRENTRABBITPOP / float(MAXRABBITPOP)
    if CURRENTRABBITPOP > 10 : # hunt
        r = random.random()
        if r < eatProb :
           CURRENTRABBITPOP -= 1
           ate = True
           rBirth = random.choice(range(3))
           if rBirth == 0 : 
              CURRENTFOXPOP += 1

    if ate == False:
       rDeath = random.choice(range(10))
       if rDeath == 0 and CURRENTFOXPOP > 10:
          # the fox died
          CURRENTFOXPOP -= 1
              
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # Your code here
    global CURRENTRABBITPOP, CURRENTFOXPOP
    foxPop = []
    rabbitPop = []
    for i in range(numSteps):
        for j in range(CURRENTRABBITPOP):
            rabbitGrowth()
        for k in range(CURRENTFOXPOP):
            foxGrowth()
        rabbitPop.append(CURRENTRABBITPOP)
        foxPop.append(CURRENTFOXPOP)
#        print "Populations: " , CURRENTRABBITPOP, CURRENTFOXPOP

    return (rabbitPop, foxPop)
        
n = 200
result = runSimulation(n)
pylab.plot(range(n), result[0], label = "Rabbits")
pylab.plot(range(n), result[1], label = "Foxes")
pylab.legend()
pylab.title ("Rabbit and Fox simulation (n = 200)")

pylab.figure()
coeff = pylab.polyfit(range(n), result[0], 2)
coeff2 = pylab.polyfit(range(n), result[1], 2)
pylab.plot(pylab.polyval(coeff, range(n)), label = "Rabbits")
pylab.plot(pylab.polyval(coeff2, range(n)), label="Foxes")
pylab.legend()
pylab.show()



