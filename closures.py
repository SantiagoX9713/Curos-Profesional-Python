def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo pueder usar palabras'
        return string * n
    return repeater


def run():
    repeat5 = make_repeater_of(5)
    print(repeat5('Hola'))


if __name__ == '__main__':
    run()