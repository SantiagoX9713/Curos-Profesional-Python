from __future__ import division


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo pueder usar palabras'
        return string * n
    return repeater


def run():
    repeat5 = make_repeater_of(5)
    print(repeat5('Hola'))



def make_division_by(n):
    return lambda x: x/n

def run1():
    division_by_3 = make_division_by(3)
    print(division_by_3(36))
    division_by_5 = make_division_by(5)
    print(division_by_5(55))
    division_by_9 = make_division_by(9)
    print(division_by_9(81))


if __name__ == '__main__':
    run()
    run1()