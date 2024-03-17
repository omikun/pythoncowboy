from util import *
import subprocess
from problem1 import *

p = None
def shell(self, arg):
    global p
    data = self.data
    p = Problem1(data)

    if arg != '':
        #assumes intent is to python3 a arg file
        print(arg)
        preamble = 'global p\n'
        print(preamble+open(arg).read())
        exec(preamble+open(arg).read())
        return

    while True:
        print_chevron()
        cmdline = input("").split(' ')
        cmd = cmdline[0]
        valid_cmds = ['ll', 'cat', 'grep', 'vim', 'radio', 'python3']
        if cmd == 'radio':
            break
        elif cmd == 'qq':
            quit()
        elif cmd == '':
            print("Want to quit? Type qq")
        elif cmd not in valid_cmds:
            print("Available commands: " + ', '.join(valid_cmds))
            continue
        elif cmd in valid_cmds:
            if len(cmdline) > 1:
                arg = 'dir/' + cmdline[1]
            else:
                arg = 'dir/'
            print(cmd + ' ' + arg)
            if cmd == 'll':
                subprocess.call(['ls', '-l', arg])
            elif cmd == 'python3':
                exec(open(arg).read())
            else:
                subprocess.call([cmd, arg])
        else:
            print("Available commands: ll, cat, grep, vim")


