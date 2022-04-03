def is_prime(number:int) -> bool:
    flag = False
    for i in range(2,number):
        if (number % i) == 0:
            flag = True
            break

def run():
    is_prime('1566')


if __name__ == '__main__':
    run()