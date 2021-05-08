from multiprocessing import Process

def square(n):
    print(f'Square is {n*n}')

def cube(n):
    print(f'Cube is {n*n*n}')

if __name__ == '__main__':
    m1 = Process(target=square,args=(10,))
    m2 = Process(target=cube,args=(10,))
    m1.start()
    m2.start()
    m1.join()
    m2.join()

    print('Done')