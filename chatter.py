from chatterbot import ChatBot

#This module is designed to allow the bot to converse in *somewhat* natural language with the user.
#It uses the ChatterBot machine learning library to accomplish this

#NOTE: The bot is very naive and susceptible to user input. It quickly learns from the user, sometimes leading to inaccuracy.
#NOTE: A vast expansion in the number of users should quickly solve this.

#UPDATE: Training has been shifted to the Ubuntu Corpus. Above mentioned problem has been slightly minimised.

class Filter(object):                                                   #required base class for writing a custom filter

    def filter_selection(self, chatterbot, session_id):
        return chatterbot.storage.base_query


class RepetitiveResponseFilter(Filter):                                 #ensures that the bot doesn't become very repetitive, at the cost of answer accuracy.

    def filter_selection(self, chatterbot, session_id):

        session = chatterbot.conversation_sessions.get(session_id)

        if session.conversation.empty():
            return chatterbot.storage.base_query

        text_of_recent_responses = []

        for statement, response in session.conversation:
            text_of_recent_responses.append(response.text)

        query = chatterbot.storage.base_query.statement_text_not_in(
            text_of_recent_responses
        )

        return query

chatbot = ChatBot(
    'SidiousBot',
    filters=["chatterbot.filters.RepetitiveResponseFilter"],              #implements the filter
    logic_adapters=[                                                      
        "chatterbot.logic.MathematicalEvaluation",                        #allows simple math to be calculated,
    #    "chatterbot.logic.TimeLogicAdapter",                             #works, but messes up response selection. Enable only for a valid reason
        "chatterbot.logic.BestMatch"
    ],
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'                 #Works! Yay! Bot training is exponentially faster now.
)

#chatbot.train('chatterbot.corpus.english')                               #Should I write a custom training module here?    #Nvm, no time left now.                    
chatbot.train()                                                           #Analysis complete. Some modifications allowed proper retrieval of responses. Major upgrade!!

def chat(update):
    return (str(chatbot.get_response(update)))
