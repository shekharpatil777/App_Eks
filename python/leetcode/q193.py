import re

def valid_phone_numbers():
    # Regex breakdown:
    # ^                     - Start of the line
    # (                     - Start of the alternation group
    #   \(\d{3}\) \d{3}-\d{4} - Format (xxx) xxx-xxxx
    #   |                   - OR
    #   \d{3}-\d{3}-\d{4}     - Format xxx-xxx-xxxx
    # )                     - End of the alternation group
    # $                     - End of the line
    pattern = r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
    
    try:
        with open('file.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if re.match(pattern, line):
                    print(line)
    except FileNotFoundError:
        pass
