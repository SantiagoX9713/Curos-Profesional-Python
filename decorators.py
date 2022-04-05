from datetime import date, datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print(f'Pasaron {str(time_elapse.total_seconds())} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,1000000):
        pass


@execution_time
def suma(a:int, b:int) -> int:
    c = a + b
    return c


if __name__ == '__main__':
    random_func()
    suma(10,15)
