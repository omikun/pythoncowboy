import time
import sys
import random
from termcolor import colored, cprint

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

cheron = colored('>', 'red', 'on_black', attrs=['reverse', 'blink'])
def print_cheron():
    cprint(cheron, end=' ')

def color_print(s):
    #print(text)
    for c in s:
        if c == ',':
            time.sleep(0.1)
        elif c == '.' or c == '?':
            time.sleep(0.2)
        cprint(c, 'green', end='')
        sys.stdout.flush()
        time.sleep(0.03 * random.randrange(1,5))
