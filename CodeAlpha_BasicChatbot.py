

def chatbot_response(user_input):
    """
    Function to return chatbot replies based on user input.
    """
    user_input = user_input.lower()
    
    if user_input in ["hello", "hi"]:
        return "Hi! How can I help you today?"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a nice day 😊"
    else:
        return "I'm sorry, I don't understand that."


def start_chatbot():
    """
    Function to start the chatbot loop.
    """
    print("🤖 Chatbot: Hello! I'm your assistant. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)
        
        if user_input.lower() in ["bye", "goodbye"]:
            break

if __name__ == "__main__":
    start_chatbot()