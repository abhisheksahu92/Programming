import random

def func1(array):
    pass


if __name__ == '__main__':
    list_of_values = random.sample(range(10,100),10)
    value = random.randint(1,len(list_of_values))
    print(f'Input: {list_of_values}')
    print(f'value is {value}')
    
