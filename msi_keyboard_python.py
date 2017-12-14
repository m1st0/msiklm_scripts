#! /usr/bin/env python3

from MsiKeyboard import MsiKeyboard
import signal

def handler(signum, frame):
    quit()

signal.signal(signal.SIGINT, handler)

if __name__ == '__main__':
    msiK = MsiKeyboard()
    msiK.smooth_flow()
