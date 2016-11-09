import sm
#so we want to extract all the comments in a file
#flip between code and comm states
class RunOfFive(sm.SM):
   startState =  0
#
#	def __init__(self,state = "notPrinted"):
#		self.startState = state

   def getNextValues(self,state,inp):
        nextState = state
        if(inp == 5):
            nextState += 1
        elif(inp != 5):
            nextState = 0
        return nextState, nextState

#str = 'def f(x): # comment\n   return 1'
#m = CommentsSM()
#print m.transduce(str)
#str = 'def f(x): # comment\n   return 1'
m = RunOfFive()
print m.transduce([2,5,0,2,5,5,0,5,7,5,5,5,5])
