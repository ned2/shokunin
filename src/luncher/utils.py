from time import time


class Timer(object):
    """Context Manager to time custom code execution"""
    
    def __init__(self, echo=False, echo_func=print):
        self.echo = echo
        self.echo_func = echo_func
        
    def __enter__(self):
        self.start = time()
        return self
    
    def __exit__(self, type, value, traceback):
        self.end = time()
        self.ellapsed = self.end - self.start
        if self.echo:
            echo_func(f"Execution took: {self.ellapsed:.2f} seconds")    
