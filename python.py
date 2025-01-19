def chatbot():
    print("Hi, I'm your simple AI chatbot! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning perfectly!")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatGPT, your simple AI assistant.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you rephrase?")
            
chatbot()
