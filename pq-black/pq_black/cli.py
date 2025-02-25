import argparse
from .formatter import format_power_query

def main():
    parser = argparse.ArgumentParser(description="Format Power Query M files.")
    parser.add_argument("file", help="Path to the Power Query M file.")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        code = f.read()
    
    formatted_code = format_power_query(code)

    with open(args.file, "w", encoding="utf-8") as f:
        f.write(formatted_code)

    print(f"Formatted {args.file}")

if __name__ == "__main__":
    main()
