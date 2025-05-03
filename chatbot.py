import random

# List of predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I assist you?"],
    "how are you": ["I'm doing great, thank you!", "I'm just a bot, but I'm good!"],
    "bye": ["Goodbye! Have a nice day!", "See you later!", "Bye! Come back soon!"],
    "default": ["Sorry, I didn't understand that.", "Can you say that again?", "I'm not sure how to respond to that."]
}

def get_response(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()
    
    # Check if the input is in predefined responses
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: " + get_response(user_input))
            break
        else:
            print("Chatbot: " + get_response(user_input))

# Run the chatbot
chatbot()