def print_tenth_line(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, 1):
                if i == 10:
                    # Strip the trailing newline if you want clean output, 
                    # but usually, we just print the line as is.
                    print(line, end='')
                    return
    except FileNotFoundError:
        pass

# Usage
print_tenth_line('file.txt')