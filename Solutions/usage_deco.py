#time spent
import os
import time
import psutil

def memory_profile():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def checktimetaken(func):
    def wraps(*args,**kwargs):
        start_time = time.time()
        mem_at_start = memory_profile()
        func(*args,**kwargs)
        mem_at_end = memory_profile()
        print(f'Time taken: {time.time() - start_time}')
        print(f'{func.__name__}: Consumed Memory: {mem_at_start},{mem_at_end},{mem_at_end - mem_at_start}')
    return wraps
