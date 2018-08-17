#===============================================================================
# DEFCON 26 Badge Hacking Fuzz Script
#
# Requirements:
#   python 2
#   `pip install pyserial`
# Usage:
#   python fuzz.py [path to device file for badge]
#===============================================================================
import random
import serial
import time
import sys

def parseArguments():
    if len(sys.argv) != 2:
        print('Usage: python ./fuzz.py [path to device file]')
        sys.exit()

def createSerialConnection():
    serialConn = serial.Serial(str(sys.argv[1]))
    serialConn.baudrate = 9600
    return serialConn

def getRandomControlChar():
    arr = ['^', 'V', '<', '>', '+', '-']
    return arr[random.randrange(0, 6)]

def fuzz():
    while(True):
        control = getRandomControlChar()
        CONN.write(b'%s' % (control))

parseArguments()
CONN = createSerialConnection()
fuzz()
