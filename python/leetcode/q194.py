def transpose_file(filename):
    with open(filename, 'r') as f:
        # Read lines and split into a 2D list
        # Example: [['name', 'age'], ['alice', '21'], ['ryan', '30']]
        matrix = [line.split() for line in f]
