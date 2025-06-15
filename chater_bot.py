from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear un nuevo chatbot
chatbot = ChatBot("AsistentePython")

# Entrenarlo con conversaciones básicas
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.spanish") 

# Probar conversación
while True:
    pregunta = input("Tú: ")
    respuesta = chatbot.get_response(pregunta)
    print(f"AsistentePython: {respuesta}")
