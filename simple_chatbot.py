# Initialization
def get_bot_response(user_message):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "tell me about place": "Sure! I can help with places. Tell me more!",
        "bye": "Goodbye! Have a great day!"
    }
    # Define Responses
    user_message = user_message.lower()
    
    # Processing User Input
    return responses.get(user_message, "Sorry, I didn't understand that.")

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    # Main interaction loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        # Get bot response and print it
        print("Chatbot:", get_bot_response(user_input))

# Exit the program
if __name__ == "__main__":
    main()
