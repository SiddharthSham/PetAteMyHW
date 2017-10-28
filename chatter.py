from chatterbot import ChatBot

#this module is designed to allow the bot to converse in natural language with the user.
#it uses the ChatterBot machine learning library to accomplish this

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

#chatbot.train('chatterbot.corpus.english')                                #uncomment before execution                     
chatbot.train()

def chat(bot,update):
    return str(chatbot.get_response(update.message.text))
