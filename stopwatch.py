import keyboard
import time
import threading
import sys


running=True
stopwatchclock=0

def stopwatch():
    global stopwatchclock
    global running
    while running:
        stopwatchclock=stopwatchclock+0.1
        time.sleep(0.1)
        stopwatch()
    print("Time!")
    print("Time: " + str(stopwatchclock))
    sys.exit(0)
def thread():
    print("Start!")
    keyboard.wait('esc')
    running=False
    print("Stop!")
    print("Time: " + str(stopwatchclock))
    sys.exit(0)

thread1=threading.Thread(target=stopwatch, daemon=True)
thread2=threading.Thread(target=thread, daemon=True)
thread2.start()
stopwatch()
