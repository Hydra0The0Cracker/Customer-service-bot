import nltk
nltk.download('punkt')

# Define responses to different inputs
responses = {
    "hi": "Hello, how can I assist you today?",
    "bye": "Goodbye, have a great day!",
    "thanks": "You're welcome!",
    "default": "I'm sorry, I don't understand. Can you please rephrase your question?"
}

# Define a function to take user input and return a response
def chatbot_response(user_input):
    # Tokenize user input into words
    words = nltk.word_tokenize(user_input.lower())
    
    # Check if user input matches any predefined responses
    for word in words:
        if word in responses:
            return responses[word]
    
    # Return default response if no match is found
    return responses["default"]

# Start the chatbot
print("Welcome to Customer Service Bot. How can I assist you today?")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    # End the conversation if user inputs "bye"
    if user_input.lower() == "bye":
        break
