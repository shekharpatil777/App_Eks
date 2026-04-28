def transpose_file(filename):
    with open(filename, 'r') as f:
        # Read lines and split into a 2D list
        # Example: [['name', 'age'], ['alice', '21'], ['ryan', '30']]
        matrix = [line.split() for line in f]

    # zip(*matrix) unpacks the rows and regroups them by index
    # result: [('name', 'alice', 'ryan'), ('age', '21', '30')]
    transposed = zip(*matrix)

    for row in transposed:
        print(" ".join(row))

# Usage
transpose_file('file.txt')