class Sentence:

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
    def processSentenceType(self):
        
        

    def __isQuestion__(self):
        if(self.stringToPrcoess.endswith('?')):
            self.isQuestion=True    #If the user was kind enough to put a ? on the end of the input we can easily decide this is a question.  Not always true but lets assume it is true for now.
        else:
            
            
    def __isArgument__(self):
        pass
    def __findSubject__(self):
        pass

