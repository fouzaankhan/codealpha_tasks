import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Loading spaCy's English model
nlp = spacy.load('en_core_web_sm')

# Defining a basic rule-based chatbot using NLTK
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name?', ['I am a chatbot created by OpenAI.', 'My name is Chatbot.']),
    (r'(.*) your favorite color?', ['I love all colors, but blue is quite nice.', 'I like all the colors of the rainbow.']),
    (r'(.*) (location|city)?', ['I am in the cloud.', 'I exist in cyberspace.']),
    (r'quit', ['Goodbye!', 'It was nice talking to you. Goodbye!']),
]

chatbot = Chat(pairs, reflections)

# Enhancing conversational ability using spaCy
def get_response(user_input):
    # Process the user input using spaCy
    doc = nlp(user_input)
    response = None

    for sent in doc.sents:
        for token in sent:
            if token.lemma_ == 'bye':
                response = "Goodbye! It was nice talking to you."
            elif token.lemma_ in ['hello', 'hi', 'hey']:
                response = "Hello! How can I help you today?"
            elif token.lemma_ == 'name':
                response = "I am a chatbot created by Fouzaan. What can I call you?"
            elif token.lemma_ == 'color':
                response = "I love all colors, but blue is quite nice."

    if response is None:
        response = "I'm not sure I understand. Can you rephrase that?"

    return response

# Combining NLTK and spaCy for enhanced conversational flow
def chatbot_response(user_input):
    # First, try to get a response using NLTK's rule-based chatbot
    nltk_response = chatbot.respond(user_input)
    if nltk_response:
        return nltk_response
    else:
        # If no suitable response is found, use spaCy to generate a response
        spacy_response = get_response(user_input)
        return spacy_response

def main():
    print("Hello! I am a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! It was nice talking to you.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
