def bubblesort(xs):
    n = len(xs)
    for i in range(n):
        for j in range(n - 1):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]

def mergesort(xs):
    pass

if __name__ == '__main__':
    print("__name__ ...")
    xs = [5, 3, 1, 2, 4, 9, 8, 5, 7]
    n = len(xs)
    bubblesort(xs)
    print(xs)

class x:
    def __init__(self, a, b, c):
    #   self.__a = a   underscores infront of the variable make it private
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return "<x a=%s, b=%s, c=%s>" % (self.a, self.b, self.c) # %s substitues the obj member variable
                                                                 # values into the string.

obj = x(3, 2.14, "cat")
print(obj) # print(obj.__str__)
obj.d = 4  # objs are dangerous because you can add variables just randomly like this. 
           # objs are hashtables in python and are dangerous becareful
print(obj.d)
