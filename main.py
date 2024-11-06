import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import random

nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('punkt')
# Create a stemmer
stemmer = PorterStemmer()

# Create a dictionary of keywords and responses
def create_dictionary():
    return {
        "hello": ["Hi", "How can I help you today?"],
        "bye": ["Goodbye", "See you later!"],
        "help": ["I can help you with various tasks. How can I assist you?"]
    }

# Function to stem words
def stem_words(words):
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

# Function to respond to user input
def respond(user_input, dictionary):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    stems = stem_words(tokens)

    for word in stems:
        if word in dictionary:
            return random.choice(dictionary[word])

    return "I'm not sure I understand. Can you rephrase that?"

# Main function
def chatbot():
    print("Hello! How can I help you today?")
    dictionary = create_dictionary()

    while True:
        user_input = input("> ")
        response = respond(user_input, dictionary)
        print(response)

        if "bye" in user_input:
            break

chatbot()

