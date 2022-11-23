# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot

import os

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer

# Clear the terminal
def clear():
    os.system("clear")

# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
			"chatterbot.corpus.english.conversations" )

clear()

# response = chatbot.get_response('What is life?')
# print(response)

response = chatbot.get_response('Who are you?')
print(response)

response = chatbot.get_response('What are you?')
print(response)
