_conversations: list[dict] = []

def log_conv(record: dict) -> None:
    _conversations.append(record)

def get_all() -> list[dict]:
    return list(_conversations)

def clear_all() -> None:
    _conversations.clear()

