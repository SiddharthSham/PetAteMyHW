from chatterbot import ChatBot

#This module is designed to allow the bot to converse in natural language with the user.
#It uses the ChatterBot machine learning library to accomplish this

#NOTE: The bot is very naive and susceptible to user input. It quickly learns from the user, sometimes leading to inaccuracy.
#NOTE: A vast expansion in the number of users should quickly solve this.

chatbot = ChatBot(
    'SidiousBot',
    #logic_adapters=[                                                     #works normally so far
    #    "chatterbot.logic.MathematicalEvaluation",
    #    "chatterbot.logic.TimeLogicAdapter",
    #    "chatterbot.logic.BestMatch"
    #],
    #input_adapter="chatterbot.input.VariableInputTypeAdapter",            #not yet tested                         
    #output_adapter="chatterbot.output.OutputAdapter", 
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'                  #does not work with ubuntu corpus. Why?
)

chatbot.train('chatterbot.corpus.english')                                #change this part to use your own training module.                    
#chatbot.train()                                                          #returns data in a funky way. Usable, but not yet. Needs more analysis.

def chat(update):
    return str(chatbot.get_response(update))
