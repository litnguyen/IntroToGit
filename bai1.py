
def isPrime(x):
    i = 2
    while (i*i < x and x % i != 0):
        i = i + 1
    if (i*i > x): return True
    else:
        return False

flag = False
while (not flag) :
    n = input('Enter positive integer: ')
    print('\n')
    num = None
    try:
        num = int(n)
    except:
        print('Enter a positive integer number:',n)
        print('\n')
        print('The number must be a positive number.')
        print('\n')
    if (num is not None and num < 0):
        print('The number must be positive.')
        print('\n')
    elif (num is not None and num > 0):
        flag = True
        print('The prime numbers from 0 to %d:' %num)
        print('\n')
        i = 2
        l = list()
        while (i < num):
            if (isPrime(i)):
                print(i,end=' ')
            i += 1
