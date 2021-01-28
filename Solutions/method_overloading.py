from multipledispatch import dispatch

@dispatch(int,int)
def add(first,second):
    print(first+second)

@dispatch(int,int,int)
def add(first,second,third):
    print(first+second+third)


add(1,2)
add(1,2,3)