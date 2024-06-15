import time

class ExcutionTimer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        end = time.pref_counter()
        print (f"{self.func.__name__}() took {(end - start) * 1000:.4f} ms")
        return result