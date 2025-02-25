import re
from typing import List, Tuple

TOKEN_TYPES = [
    ("KEYWORD", r"\b(let|in|each|if|then|else|type|meta|as)\b"),
    ("OPERATOR", r"[=,\{\}\[\]\(\)\+\-\*/&]"),
    ("STRING", r"\".*?\""),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("WHITESPACE", r"\s+"),
    ("COMMENT", r"//.*?$"),
]

TOKEN_REGEX = re.compile("|".join(f"(?P<{name}>{regex})" for name, regex in TOKEN_TYPES), re.MULTILINE)

class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

def tokenize(code: str) -> List[Token]:
    tokens = []
    for match in TOKEN_REGEX.finditer(code):
        for name, _ in TOKEN_TYPES:
            if match.group(name):
                tokens.append(Token(name, match.group(name)))
                break
    return tokens
