import keyboard
import time
import sys
import signal

count = 0

while(count != int(sys.argv[2]) * 2):
    time.sleep(0.5)
    keyboard.write(sys.argv[1])
    count = count + 1
