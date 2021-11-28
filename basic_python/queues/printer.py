import random
from basic_python.queues.queue import Queue

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

def simulation(num_seconds, pages_per_minute):
    pass

def new_print_task():
    pass
