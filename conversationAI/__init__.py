

#Written By Andrew Allard
#
#Attempting to create an AI for conversation.
#This is going to have to take in sentences (text based at first) Process what is being said and or implied.
#Based on the context of the conversation being had, form and deliver a logical responce that is approprite to the conversation.
#
#
#This is hopefully going to become an intellagent agent capable of holding a logical conversation.
#


self._version='0'



class conversation:
    def __init__(self):
        self._typesOfConversation=conversationTypes
        self._CurrentConversationType=self._typesOfConversation.GENERAL
        self._PreviousTypesOfConversations=None
        self._subject=None




class converstationTypes:
    def __init__(self):
        
        self.GENERAL=0
        self.ARGUMENT=1
        self.DEBATE=2
        self.COMFORT=3
        self.PLAYFUL=4
        self.PUNISHMENT=5
        self.

class sentence:

    _types=('Question','Statement')
    _StatementTypes('Argumentive')

    def __init__(self,stringIn):
        assert isinstance(stringIn,str)
        self.stringToPrcoess=stringIn
        self.isQuestion=None
        self.isArgumentive=None
        self.subject=None
        self.isActive=None
        self.Action=None
        self.evidence=None
        

    def __isQuestion__(self):
        if(self.stringToPrcoess.endswith('?')):
            self.isQuestion=True    #If the user was kind enough to put a ? on the end of the input we can easily decide this is a question.  Not always true but lets assume it is true for now.
        else:
            
            
    def __isArgument__(self):
        pass
    def __findSubject__(self):
        pass

    def 









