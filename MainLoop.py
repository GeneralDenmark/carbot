from Meter import initialize
import random
import time
import threading
import queue
from doTalk import do_talk

meters = \
    {
        0: {'height': 200, 'width': 200, 'text': '1', 'meter': None},
        1: {'height': 200, 'width': 200, 'text': '2', 'meter': None},
        2: {'height': 200, 'width': 200, 'text': '3', 'meter': None},
    }

meters, app = initialize(meters)
speaking = False


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        speaking = True
        do_talk(item)
        speaking = False
        q.task_done()


q = queue.Queue()

talker = threading.Thread(target=worker)
talker.start()

while 1:
    meter1 = 0
    meter2 = 0

    if app.is_alive():
        if meters.get(0).get('meter'):
            increment = random.randint(-30, 30)
            while 300 < meter1 + increment < 0:
                increment = random.randint(-30, 30)

            meter1 = meter1 + increment
            meters[0]['meter'].set(meter1 + increment)
            if not speaking:
                q.put("New speed for meter " + meters.get(0).get('text') + ". New speed is: " + str(meter1))

        if meters.get(1).get('meter'):
            increment = random.randint(-30, 30)
            while 300 < meter2 + increment < 0:
                increment = random.randint(-30, 30)

            meter2 = meter2 + increment
            meters[1]['meter'].set(meter2 + increment)
            if not speaking:
                q.put("New speed for meter " + meters.get(1).get('text') + ". New speed is: " + str(meter2))
    else:
        break
    time.sleep(1.05)  # Required as there is some trouble killing the threads if there is no sleep.
