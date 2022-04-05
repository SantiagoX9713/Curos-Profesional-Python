# my_list = [1,2,3,4,5,6,7,8,9]
# my_iter = iter(my_list)

# print(my_iter)
# print(type(my_iter))

# print(next(my_iter))


# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break

# # Básicamente eso es lo que hace un ciclo for
# for element in my_list:
#     print(my_list.index(element) + 1)


# class EvenNumbers:
#     def __init__(self,max=None):
#         self.max = max
    
#     def __iter__(self):
#         self.num = 0
#         return self
    
#     def __next__(self):
#         if not self.num or self.num <= self.max:
#             result = self.num
#             self.num += 2
#             return result
#         else:
#             raise StopIteration

import time

class FiboIter():
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.n2


if __name__ == '__main__':
    fibonacci = FiboIter()
    for i in fibonacci:
        print(i)
        time.sleep(0.5)