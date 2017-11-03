#################################################################################
#Written By Andrew Allard as part of the attempt to make an intelligent agent
#one can have a conversation with.
#


class Word:
    __version='0'
    def __init__(self):
        self.isNoun=False
        self.isArticle=False
        self.isVerb=False
        self.isAdverb=False
        
    

    
class WordTypes:
    NOUN=0
    VERB=1
    ARTICLE=2
    ADJECTIVE=3
    ADVERB=4
    
    def __init__(self):
        self.NOUN=0
        self.VERB=1
        self.ARTICLE=2
        self.ADJECTIVE=3
        self.ADVERB=4
