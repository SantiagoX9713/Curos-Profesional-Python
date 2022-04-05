my_list = [1,2,3,4,5,6,7,8,9]
my_iter = iter(my_list)

print(my_iter)
print(type(my_iter))

print(next(my_iter))


while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# Básicamente eso es lo que hace un ciclo for
for element in my_list:
    print(my_list.index(element) + 1)


class EvenNumbers:
    def __init__(self,max=None):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.num or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration