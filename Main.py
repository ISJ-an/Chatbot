import nltk
from nltk.chat.util import Chat, reflections

# Ensure you have downloaded the necessary NLTK resources
nltk.download('punkt')  # Required for tokenization in NLTK

# Define a list of patterns and responses
patterns_responses = [
    (r'Hi|Hello|Hey', 'Hello! How can I assist you today?'),
    (r'What is your name?', 'I am a chatbot created using NLTK.'),
    (r'How are you?', 'I am just a program, but I am functioning well. How can I help you?'),
    (r'What can you do?', 'I can respond to a few predefined questions. Ask me something!'),
    (r'Bye|Goodbye', 'Goodbye! Have a great day!')
]

# Create a Chat object
chatbot = Chat(patterns_responses, reflections)

# Function to interact with the chatbot
def chat_with_bot():
    print("Hello! I am your chatbot. Type 'Bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)
        if response in ['Goodbye! Have a great day!', 'Bye']:
            break

# Run the chatbot
if __name__ == "__main__":
    chat_with_bot()
