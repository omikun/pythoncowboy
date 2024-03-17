from util import *
from shell import shell

def interact():
    import code
    code.InteractiveConsole(locals=globals()).interact()

class Cowboy:
    code_snippet = ''
    data = dict()
    def processLine(self, line):
        pprint = color_print
        data = self.data

        #print(line)
        if line[0] == '#':
            return
        elif line[0] == '>':
            print_chevron()
            key = line[1:].replace('\n', '')
            data[key] = input("")
            #print("got > " + key + " : " + str(type(data[key])) + " : " + data[key])
        elif line[0] == '%':
            shell(self, line[1:-1])
        elif line[0] == '<':
            self.code_snippet += line[1:]
        elif line[0] == '~':
            self.code_snippet += line[1:-1]
            #print('executing code,')
            #print(self.code_snippet)
            exec(self.code_snippet)
            self.code_snippet = ''
        elif '$' in line:
            segments = line[:-1].split('$')
            #print(segments)
            for i,s in enumerate(segments):
                if ' ' not in s and len(s) > 0:
                    segments[i] = data.setdefault(s, 'uninitialized')
            for s in segments:
                pprint(s)
            print('')
        else:
            pprint(line)

cb = Cowboy();
with open("script.pycb") as f:
    for line in f:
        cb.processLine(line)
quit()
