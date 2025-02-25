from .parser import tokenize

INDENT_SIZE = 4  # Number of spaces per indentation level

def format_power_query(code: str) -> str:
    """Format Power Query M code with improved indentation."""
    tokens = tokenize(code)
    formatted_tokens = []
    indent_level = 0
    new_line = False
    inside_record = False

    for i, token in enumerate(tokens):
        if token.type == "KEYWORD":
            formatted_tokens.append(token.value.lower())  # Enforce lowercase for keywords

        elif token.type == "OPERATOR":
            if token.value in "{[":
                indent_level += 1
                formatted_tokens.append(token.value)
                inside_record = token.value == "{"  # Track if we're inside a record
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level))
            elif token.value in "}]":
                indent_level = max(0, indent_level - 1)
                inside_record = False
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)
            else:
                formatted_tokens.append(token.value)

        elif token.type == "WHITESPACE":
            continue  # Skip whitespace

        elif token.type == "COMMENT":
            formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)

        else:  # Identifiers, numbers, strings
            if new_line or inside_record:
                formatted_tokens.append("\n" + " " * (INDENT_SIZE * indent_level) + token.value)
                new_line = False
            else:
                formatted_tokens.append(token.value)

        # Handle adding new lines after a comma inside a record
        if token.type == "OPERATOR" and token.value == ",":
            if inside_record:
                formatted_tokens.append(token.value)
                new_line = True
            else:
                formatted_tokens.append(token.value + " ")

    formatted_code = "".join(formatted_tokens)
    return formatted_code.strip()

if __name__ == "__main__":
    sample_code = """let
    Source = Table.FromRecords({[Name="Alice", Age=25], [Name="Bob", Age=30]}),
    Filtered = Table.SelectRows(Source, each [Age] > 26)
in
    Filtered"""

    formatted = format_power_query(sample_code)
    print(formatted)
