#!/usr/bin/python
#
# repeat.py
#
# Repeat command N times every S seconds.
#

import argparse
from time import sleep
from subprocess import Popen

parser = argparse.ArgumentParser(description='Repeat job N times per S seconds.')
parser.add_argument('-n', type=int, default=10, help='Will repeat N times. (default=10)')
parser.add_argument('-s', type=int, default=1, help='Will repeat per S seconds. (default=1)')
parser.add_argument('cmd', nargs=argparse.REMAINDER, help='Command to be repeated.')


def repeat(cmds, n=10, s=1):
    for _ in xrange(n):
        Popen(cmds)
        sleep(s)


def main():
    args = parser.parse_args()
    if len(args.cmd):
        repeat(args.cmd, args.n, args.s)
    else:
        print 'Nothing to run. Stopped.'


if __name__ == '__main__':
    main()
