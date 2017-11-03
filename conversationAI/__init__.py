

#Written By Andrew Allard
#
#Attempting to create an AI for conversation.
#This is going to have to take in sentences (text based at first) Process what is being said and or implied.
#Based on the context of the conversation being had, form and deliver a logical responce that is approprite to the conversation.
#
#
#This is hopefully going to become an intellagent agent capable of holding a logical conversation.
#


self.__version='0'



class Conversation:
    def __init__(self):
        self._typesOfConversation=conversationTypes
        self._CurrentConversationType=self._typesOfConversation.GENERAL
        self._PreviousTypesOfConversations=None
        self._subject=None




class ConverstationTypes:
    GENERAL=0
    ARGUMENT=1
    DEBATE=2
    COMFORT=3
    PLAYFUL=4
    PUNISHMENT=5
    
    def __init__(self):
        
        self.GENERAL=0
        self.ARGUMENT=1
        self.DEBATE=2
        self.COMFORT=3
        self.PLAYFUL=4
        self.PUNISHMENT=5
        self.type=ConversationTypes.GENERAL

        

