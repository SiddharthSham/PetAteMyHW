from chatterbot import ChatBot

#This module is designed to allow the bot to converse in *somewhat* natural language with the user.
#It uses the ChatterBot machine learning library to accomplish this

#NOTE: The bot is very naive and susceptible to user input. It quickly learns from the user, sometimes leading to inaccuracy.
#NOTE: A vast expansion in the number of users should quickly solve this.

#UPDATE: Training has been shifted to the Ubuntu Corpus. Above mentioned problem has been slightly minimised.

chatbot = ChatBot(
    'SidiousBot',
    #logic_adapters=[                                                     #works normally so far
    #    "chatterbot.logic.MathematicalEvaluation",
    #    "chatterbot.logic.TimeLogicAdapter",
    #    "chatterbot.logic.BestMatch"
    #],
    trainer='chatterbot.trainers.UbuntuCorpusTrainer'                     #Works! Yay! Bot training is exponentially faster now.
)

#chatbot.train('chatterbot.corpus.english.conversations')                 #Should I write a custom training module here?    #Nvm, no time left now.                    
chatbot.train()                                                           #Analysis complete. Some modifications allowed proper retrieval of responses. Major upgrade!!

def chat(update):
    return (str(chatbot.get_response(update)))
