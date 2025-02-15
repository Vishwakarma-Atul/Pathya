
import re
# import yaml
# from pathlib import Path

# def load_intents():
#     config_path = Path(__file__).parent.parent / "config" / "intents.yaml"
#     with open(config_path) as f:
#         intents = yaml.safe_load(f)["intents"]
#     return intents

# INTENT_PATTERNS = load_intents()
INTENT_PATTERNS = {
    "order_status": [r"where is my order", r"track my order", r"order status"],
    "order_details": [r"order details for (\d+)", r"order (\d+) info"],
}

def match_intent(user_message: str):
    user_message = user_message.lower()
    for intent, patterns in INTENT_PATTERNS.items():
        for pattern in patterns:
            match = re.search(re.compile(pattern), user_message)
            if match:
                return intent, match.groups()
    return None, None
