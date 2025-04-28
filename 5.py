import nltk
from nltk.chat import Chat
reflections = {
    "i am": "you are",
    "i'm": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
    "am": "are",
    "are": "am"
}


pairs = [
    [r"hi|hey|hello(.*)", ["Hello! How can I help you today?", "Hey there!"]],
    [r"what is your name?", ["I am a chatbot created to help you!"]],
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"how are you(.*)", ["I'm doing great! How about you?"]],
    [r"sorry(.*)", ["It's okay, no worries!"]],
    [r"I am feeling (.*)", ["Why are you feeling %1?", "It's normal to feel %1 sometimes."]],
    [r"I feel (.*)", ["Why do you feel %1?", "What made you feel %1?"]],
    [r"i want (.*)", ["Why do you want %1?", "Would getting %1 make you happy?"]],
    [r"(.*) your hobbies?", ["I like chatting with humans like you!", "My hobby is learning and talking."]],
    [r"(.*)weather(.*)", ["I'm a bot, but I hope the weather is nice where you are!"]],
    [r"(.*)help(.*)", ["Of course, I'm here to help. Tell me more!"]],
    [r"quit", ["Bye-bye! Have a great day!"]],
    [r"bye(.*)", ["Goodbye! It was nice talking to you."]],
    [r"(.*)", ["That's interesting. Tell me more!", "I see. What else?", "Could you explain that further?"]]
]


def chat():
    print("Hii there I am chatbot")
    chat = Chat(pairs,reflections)
    chat.converse() # by help of converse it Starts an interactive loop

chat()