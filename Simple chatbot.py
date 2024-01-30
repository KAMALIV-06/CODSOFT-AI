import re

def rule_based_chatbot(user_input):
    # Define rules and corresponding responses
    rules = [
        {'pattern': r'hello|hi|hey', 'response': 'Hello! How can I help you?'},
        {'pattern': r'how are you', 'response': 'I am a computer program, so I don\'t have feelings, but thanks for asking!'},
        {'pattern': r'bye|goodbye', 'response': 'Goodbye! Have a great day!'},
        {'pattern': r'name', 'response': 'I am a chatbot. You can call me ChatGPT.'},
        {'pattern': r'help', 'response': 'I can assist you with general information. Ask me anything!'}
    ]

    # Check user input against rules
    for rule in rules:
        if re.search(rule['pattern'], user_input, re.IGNORECASE):
            return rule['response']

    # Default response if no rule matches
    return 'I\'m sorry, I didn\'t understand that. Could you please ask another question?'

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = rule_based_chatbot(user_input)
    print("Bot:", response
