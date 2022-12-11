from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('Mrchat')
trainer = ChatterBotCorpusTrainer(chatbot)

#next statement in the list is considered as the ans for previous statement

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

exit_conditions = ('exit','quit')
print("\n------------------\n Hi Iam Mrchat\n------------------\n")
while True:
    query = input(">")
    if query in exit_conditions:
        break
    else:
        print(f"{chatbot.get_response(query)}")