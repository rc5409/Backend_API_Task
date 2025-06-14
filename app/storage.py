conversation_log = []

def log_conversation(prompt, response):
    conversation_log.append({"prompt": prompt, "response": response})

def get_conversations():
    return conversation_log

def clear_conversations():
    conversation_log.clear()