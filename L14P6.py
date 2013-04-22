import random


def drawBallsFromBucket():
     bucket = [ 'W' * 10]
     bucket.extend
     bucket = ['R', 'R', 'R', 'G', 'G', 'G']
     drawn = []
     for i in range(3):
         choice = random.choice(bucket)
         bucket.remove(choice)
         drawn.append(choice)

     #print drawn

     if drawn[0] == drawn[1] == drawn[2]:
         return 1
     else:
         return 0


         
        
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    successfulTrials = 0
    for i in range(numTrials):
        successfulTrials += drawBallsFromBucket()

    #print "successful Trials = " + str(successfulTrials)

    return float(successfulTrials) / float(numTrials)

        

         
         


        
