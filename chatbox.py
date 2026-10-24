"""
Task 1: Chatbot with Rule-Based Responses
"""

RULES = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! How can I assist you?",
    "help": "I can answer basic questions. Try asking about my name or purpose.",
    "name": "My name is SAM Bot, a rule-based assistant.",
    "purpose": "I am designed to demonstrate rule-based responses."
}

def get_response(user_input):
    user_input = user_input.lower()
    for keyword, response in RULES.items():
        if keyword in user_input:
            return response
    return "Sorry, I did not understand. Please try again."

if __name__ == "__main__":
    print("SAM Bot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.lower() in ["bye", "exit", "quit"]:
            print("SAM Bot: Goodbye!")
            break
        print("SAM Bot:", get_response(user))

