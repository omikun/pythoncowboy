from util import *
import subprocess

def shell():
    while True:
        print_chevron()
        cmdline = input("").split(' ')
        cmd = cmdline[0]
        valid_cmds = ['ll', 'cat', 'grep', 'vim', 'radio']
        if cmd == 'radio':
            break
        elif cmd == 'qq':
            quit()
        elif cmd == '':
            print("Want to quit? Type qq")
        elif cmd not in valid_cmds:
            print("Available commands: ll, cat, grep, vim")
            continue
        elif cmd in valid_cmds:
            if len(cmdline) > 1:
                arg = 'dir/' + cmdline[1]
            else:
                arg = 'dir/'
            print(cmd + ' ' + arg)
            if cmd == 'll':
                subprocess.call(['ls', '-l', arg])
            else:
                subprocess.call([cmd, arg])
        else:
            print("Available commands: ll, cat, grep, vim")


