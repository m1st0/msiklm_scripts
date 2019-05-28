#! /usr/bin/env python3

from MsiKeyboard import MsiKeyboard
import signal
#import os
from sys import exit

def handler(signum, frame):
    sys.exit(signum)

signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':
    #os.chdir(os.path.dirname(sys.argv[0]))
    msiK = MsiKeyboard()
    #msiK.random_wave()
    msiK.smooth_flow()
