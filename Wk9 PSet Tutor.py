import sm

class CM(sm.SM):

	def __init__(self,state = 0):
		self.startState = state

	def getNextValues(self,state,inp):
	    outp = [(state+inp),'--',inp]
	    if(outp[0] >= 100):
	        #get coek
	        outp[2] = outp[0] - 100
	        outp[0] = 0
	        nextState = outp[0] 
	        outp[1] = "coke"
	    elif (inp == 50 or inp == 100):
	        outp[2] = 0
	        nextState = state + inp
	    elif (inp != 50 or inp != 100):
	        outp[0] = 0
	        outp[2] = inp
	        nextState = outp[0]	    
	    print tuple(outp)
	    return nextState,tuple(outp)


c=CM()
c.start()
c.step(50)
(50, '--', 0)
c.step(50)
(0, 'coke', 0)
c.step(100)
(0, 'coke', 0)
c.step(10)
(0, '--', 10)
c.step(50)
(50, '--', 0)
c.step(100)
(0, 'coke', 50)
c.step(10)
(0, '--', 10)