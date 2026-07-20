print("🤖 Chatbot: Welcome!")
print("Type 'help' to see available commands.")
print("Type 'exit' to end the conversation.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        print("🤖 Chatbot: Hello! Nice to meet you.")

    # Identity
    elif user in ["what is your name", "who are you", "your name"]:
        print("🤖 Chatbot: I am RuleBot, a simple AI chatbot.")

    # Creator
    elif user in ["who created you", "who made you"]:
        print("🤖 Chatbot: I was created using Python.")

    # Well-being
    elif user in ["how are you", "how are you doing"]:
        print("🤖 Chatbot: I am doing great. Thanks for asking!")

    # User name
    elif user == "my name is vipin":
        print("🤖 Chatbot: Nice to meet you, Vipin!")

    # Time
    elif user == "what time is it":
        print("🤖 Chatbot: Sorry, I cannot tell the current time.")

    # Date
    elif user == "what is today's date":
        print("🤖 Chatbot: Sorry, I cannot access today's date.")

    # AI
    elif user == "what is ai":
        print("🤖 Chatbot: AI stands for Artificial Intelligence.")

    # Python
    elif user == "what is python":
        print("🤖 Chatbot: Python is a popular programming language.")

    # College
    elif user == "which language are you written in":
        print("🤖 Chatbot: I am written in Python.")

    # Motivation
    elif user in ["motivate me", "motivation"]:
        print("🤖 Chatbot: Believe in yourself. Keep learning every day!")

    # Joke
    elif user == "tell me a joke":
        print("🤖 Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Help
    elif user == "help":
        print("""
Available Commands:
- hi / hello / hey
- how are you
- who are you
- what is your name
- who created you
- what is ai
- what is python
- which language are you written in
- tell me a joke
- motivate me
- bye
- exit
        """)

    # Thanks
    elif user in ["thanks", "thank you"]:
        print("🤖 Chatbot: You're welcome!")

    # Bye
    elif user in ["bye", "goodbye"]:
        print("🤖 Chatbot: Goodbye! Have a wonderful day!")

    # Exit
    elif user == "exit":
        print("🤖 Chatbot: Chat ended. See you again!")
        break

    # Unknown command
    else:
        print("🤖 Chatbot: Sorry, I don't understand. Type 'help' to see available commands.")