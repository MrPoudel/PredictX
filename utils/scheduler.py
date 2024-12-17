import time

def schedule_task(interval, task, *args):
    while True:
        task(*args)
        time.sleep(interval * 60)
