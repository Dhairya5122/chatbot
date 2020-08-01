import nltk
from nltk.chat.util import Chat, reflections
print(Chat)
reflections
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a Dhairya Shah chatbot ?",]
    ],
    [
        r"Who are you?",
        ["You can call me a chatbot",]
    ],
    [
        r"Who make you|who is your creator",
        ["I am chatbot, My creator name is Sir, DHAIRYA SHAH!!",]
    ],
    [
        r"What is your brithdate|what is your brith date|what is your DOB|what is your date of brith",
        ["My Brithdate is 30 July 2020",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"I am fine",
        ["great to hear that, how can i help you?",]
    ],

    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"how you can help me ",
        ["I can do anything for you just give me a command",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit|bye|goodbye",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatbot():
        print("Hi, I'm the chatbot. Made by Dhairya Shah") 

chatbot()

chat = Chat(set_pairs, reflections)
print(chat)
chat.converse()
if __name__ == "__main__":
    chatbot()












