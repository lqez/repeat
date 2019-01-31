#!/usr/bin/python
#
# repeat.py
#
# Repeat command N times every S seconds.
#

from datetime import datetime
from ptimer import repeat
from subprocess import Popen
import argparse


parser = argparse.ArgumentParser(description='Repeat job N times per S seconds.')
parser.add_argument('-n', type=int, default=10, help='Will repeat N times. (default=10, infinite=0)')
parser.add_argument('-s', type=int, default=1, help='Will repeat per S seconds. (default=1)')
parser.add_argument('-v', help='Print datetime on every run. (default=False)', action='store_true')
parser.add_argument('cmd', nargs=argparse.REMAINDER, help='Command to be repeated.')


def main():
    args = parser.parse_args()

    def run():
        if args.v:
            print(datetime.now())
        Popen(args.cmd)

    if len(args.cmd):
        repeat(run, args.n if args.n > 0 else -1, args.s)
    else:
        print('Nothing to run. Stopped.')


if __name__ == '__main__':
    main()
