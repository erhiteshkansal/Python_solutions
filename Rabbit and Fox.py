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
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    z1=CURRENTRABBITPOP
    for i in range(0,z1):
        p=1.0-(CURRENTRABBITPOP/(MAXRABBITPOP*1.0))
        x=random.random()
        if x<=p:
            CURRENTRABBITPOP=CURRENTRABBITPOP+1
                                       
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
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    peat= CURRENTRABBITPOP/(MAXRABBITPOP*1.0)
    x=random.random()
    z1=CURRENTFOXPOP
    for k in range(0,z1):
        if x<=peat and CURRENTRABBITPOP>=11:
            CURRENTRABBITPOP=CURRENTRABBITPOP-1
            y=random.random()
            if y<=(1/(3.0)):
                CURRENTFOXPOP=CURRENTFOXPOP+1
        elif CURRENTFOXPOP>=11:
            y=random.random()
            if y<=0.9:
                CURRENTFOXPOP=CURRENTFOXPOP-1
               
                        
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    i=0
    r=[]
    f=[]
    while i<numSteps:
        i=i+1
        rabbitGrowth()
        foxGrowth()
        r.append(CURRENTRABBITPOP)
        f.append(CURRENTFOXPOP)
    pylab.figure(1)
    pylab.plot(r,"ro")
    coeff = pylab.polyfit(range(len(r)), r, 2)
    pylab.plot(pylab.polyval(coeff, range(len(r))))
    pylab.figure(2)
    pylab.plot(f,"bo")
    coeff1 = pylab.polyfit(range(len(f)), f, 2)
    pylab.plot(pylab.polyval(coeff1, range(len(f))))
    pylab.show()
    
    
runSimulation(200)                              
            
        