# read file and split by line and save as json


with open('sample.json', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
  with open('./sample/file_{}.json'.format(i), 'w') as f:
    f.write(line)

