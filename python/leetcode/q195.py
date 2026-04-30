def print_tenth_line(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
