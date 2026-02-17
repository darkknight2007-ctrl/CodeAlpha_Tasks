import random
def f_responses(user_input):
    responses = {
        "hello": [
            "Hi there! How can I help you today?",
            "Hello! Ready to chat.",
            "Hey! What's on your mind?",
            "Greetings, human!",
            "Hi! It's good to see you."
        ],
        "hi": [
            "Hi there!",
            "Hello!",
            "Hey! How are things?"
        ],
        "how are you": [
            "I'm operating at 100% efficiency!",
            "Doing well, thanks for asking.",
            "I'm just code, but I'm feeling great!",
            "All systems nominal.",
            "I'm excellent! How about you?"
        ],
        "bye": [
            "Goodbye! Have a great day.",
            "See you next time!",
            "Signing off. Take care!",
            "Bye for now!",
            "Catch you later!"
        ],
        "who are you": [
            "I am a simple Python chatbot.",
            "I'm your friendly neighborhood code-bot.",
            "Just a script living in your terminal.",
            "I'm an AI in training.",
            "I'm a bot created to chat with you."
        ],
        "tell me a joke": [ #some lame jokes
            "Why did the Python programmer wear glasses? Because he couldn't C#.",
            "There are 10 types of people: those who understand binary, and those who don't.",
            "Why was the computer cold? It left its Windows open."
        ],
        "dark joke": [ # I would not call them lame but kinda dark
            "who are the fastest readers in history? THE 9/11 VICTIMS BECAUSE THEY WENT DOWN MULTIPLE STORIES IN MERE SECONDS",
            "whats the last name of obama? its obama!",
            "i have many jokes on unemployed people but most of them dont work!"
        ]
    }
#the user input
    key = user_input.lower().strip()

    if key in responses:
        #random module for random responses
        return random.choice(responses[key])
    else:
        return "I don't understand."


def start_chat():
    print("--- Chatbot (Type 'bye' to exit) ---")

    while True:
        user_text = input("You: ")

        reply = f_responses(user_text)
        print(f"Bot: {reply}")

        # Exit condition
        if user_text.lower().strip() == "bye":
            break


if __name__ == "__main__":
    start_chat()
