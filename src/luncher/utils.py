from time import time
from random import random
from cProfile import Profile


def randrange(maximum):
    """Returns a pseudo-random integer between zero and the supplied maximum"""
    return round(random()*maximum)


class Timer:
    """Context Manager to time custom code execution"""
    
    def __enter__(self):
        self.start = time()
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time()
        self.ellapsed = self.end - self.start


class Profiler:
    """Context Manager for cProfile.Profile (not enabled in cProfile until 3.8)"""

    def __enter__(self):
        self.profile = Profile()
        self.profile.enable()
        return self.profile
    
    def __exit__(self, type, value, traceback):
        self.profile.disable()

    
