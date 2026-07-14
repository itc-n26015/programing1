with open('sample.txt', 'w') as f:
    f.write('test')


with open('sample.txt', 'r') as f:
    line = f.readline()
    print(line)
