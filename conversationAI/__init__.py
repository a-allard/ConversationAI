











class processType:

    _types=('Question','Statement')
    _StatementTypes('Objective','Subjective','Argumentative','Theorizing','Definative')

    def __init__(statemnet):
        assert isinstance(statement,str)
        self.statement=statement
        pass

    def isQuestion(self):
        
