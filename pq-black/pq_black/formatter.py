from .parser import tokenize

INDENT_SIZE = 4  # Number of spaces per indentation level

def format_power_query(code: str) -> str:
    """Format Power Query M code with improved indentation and no duplicate commas."""
    tokens = tokenize(code)
    formatted_tokens = []
    indent_level = 0
    new_line = False
    inside_record = False
    last_token = None  # Track previous token to prevent duplicate commas

    for i, token in enumerate(tokens):
        if token.type == "KEYWORD":
            formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value.lower())  # Ensure lowercase keywords

        elif token.type == "OPERATOR":
            if token.value in "{[":
                indent_level += 1
                formatted_tokens.append(token.value)
                inside_record = token.value == "{"  # Track if we're inside a record
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level))  # Indent after opening brace
            elif token.value in "}]":
                indent_level = max(0, indent_level - 1)
                inside_record = False
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)
            elif token.value == ",":
                if last_token and last_token.value == ",":  # Prevent duplicate commas
                    continue
                formatted_tokens.append(token.value)
                if inside_record:  # Ensure new line after a comma inside records
                    formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level))
            else:
                formatted_tokens.append(token.value)

        elif token.type == "WHITESPACE":
            continue  # Skip unnecessary whitespace

        elif token.type == "COMMENT":
            formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)

        else:  # Identifiers, numbers, strings
            if new_line or inside_record:
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)
                new_line = False
            else:
                formatted_tokens.append(" " + token.value)

        last_token = token  # Store last token for duplicate checks

    formatted_code = "".join(formatted_tokens).strip()
    return formatted_code

if __name__ == "__main__":
    sample_code = """let
    Source = Table.FromRecords({[Name="Alice", Age=25], [Name="Bob", Age=30]}),
    Filtered = Table.SelectRows(Source, each [Age] > 26)
in
    Filtered"""

    formatted = format_power_query(sample_code)
    print(formatted)
