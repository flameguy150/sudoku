from time import perf_counter

class Timer:
    def __init__(self):
        self.total_time = 0
        self.start_time = 0
        self.running = False

    def start(self):
        if self.running == False:
            self.running = True
            self.start_time = perf_counter()

    def stop(self):
        if self.running == True:
            self.total_time += perf_counter() - self.start_time
            self.running = False

    def elapsed(self):
        if self.running:
            return self.total_time + (perf_counter() - self.start_time)
        else:
            return self.total_time

    def reset(self):
        self.total_time = 0
        self.running = False

