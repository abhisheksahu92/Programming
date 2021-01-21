def fabonacci(nums):
    x,y = 0,1
    for _ in range(nums):
        print(x)
        x,y = y,x+y
          
if __name__ == '__main__':
    list_of_values = [12]
    
    for li in list_of_values:
        print(f'Input is {li}')
        fabonacci(li)