from sql_app.models import Message
from transformers import pipeline

classifier = pipeline(task="sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def message_analyses(message: Message):
    
    score = classifier(message.content)

    if (score.label == "1 star"):
        # send to BD
        pass
    
