






class conversation:
    def __init__(self):
        self._typesOfConversation=('General','Argument','Debate','Comfort','Playful','Punishment')
        self._CurrentConversationType=self._typeOfConversation(0)
        self._PreviousTypesOfConversations=None






class processType:

    _types=('Question','Statement')
    _StatementTypes('Objective','Subjective','Argumentative','Theorizing','Definative')

    def __init__(self,stringIn):
        assert isinstance(stringIn,str)
        self.stringToPrcoess=stringIn
        self.isQuestion=None
        self.isArgument=None

    def isQuestion(self):
        if(self.stringToPrcoess.endswith('?')):
            self.isQuestion=True    #If the user was kind enough to put a ? on the end of the input we can easily decide this is a question.  Not always true but lets assume it is true for now.
            
