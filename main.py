from util import *

pprint = color_print
data = dict()
with open("text.csv") as f:
    for line in f:
        if line[0] == '>':
            print_cheron()
            data[line[1:-1]] = input("")
        elif '$' in line:
            segments = line.split('$')
            for i,s in enumerate(segments):
                 if ' ' not in s and len(s) > 0:
                    segments[i] = data[s]
            for s in segments:
                pprint(s)
        else:
            pprint(line)

quit()
