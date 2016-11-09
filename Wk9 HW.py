import sm
#so we want to extract all the comments in a file
#flip between code and comm states
class FirstWordSM(sm.SM):
        startState = 'notPrinted'
        
	def __init__(self,state = "notPrinted"):
		self.startState = state

	def getNextValues(self,state,inp):
	    returned = None
	    if(inp == "\n"):
	        state = "notPrinted"
	        #returned = None
	    elif (inp == " " and state == "notPrinted"):
                pass
	        #returned = None    
	    elif (inp == " " and state == "printed"):
                state = "stop"
	        #returned = None
	    else:
	        if (state == "notPrinted"):
	            state = "printed"
	        if (state != "stop"):
	           returned = inp
	    return state,returned

#str = 'def f(x): # comment\n   return 1'
#m = CommentsSM()
#print m.transduce(str)
str = 'def f(x): # comment\n   return 1'
m = FirstWordSM()
print m.transduce(str)