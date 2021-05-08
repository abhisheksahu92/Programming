#multiple decorator
import time,os,psutil

#create full name
def getTime(func):
    def wraps(*args):
        print('Mr.',end=' ')
        func()
        print('Sahu')
    return wraps

@getTime
def propername():
    print('Abhishek',end=' ')

#propername()

# add 2 to every element of list
def addtwo(func):
    def wraps(*args):
        return func(*args) + 2
    return wraps

@addtwo
def listofnumber(number):
    return number

for x in range(10):
    print(listofnumber(x))


#time spent
def checktimetaken(func):
    def wraps(*args):
        start_time = time.time()
        func()
        return f'Time taken: {time.time() - start_time}'
    return wraps

@checktimetaken
def passtime():
    for _ in range(100000):
        pass

print(passtime())

#Memory took
def memory_profile():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def profile(func):
    def wraps(*args,**kwargs):
        mem_at_start = memory_profile()
        func()
        mem_at_end = memory_profile()
        return f'{func.__name__}: Consumed Memory: {mem_at_start},{mem_at_end},{mem_at_end-mem_at_start}'
    return wraps

@profile
def extensive_processing():
    x = [1] * (10 ** 7)
    y = [2] * (4 * 10 ** 8)
    del x

print(extensive_processing())