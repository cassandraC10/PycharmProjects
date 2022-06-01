for lst in [1,2,3,4,5]:
    print(lst)

def custom_for(iterable):
    it = iter(iterable)

def custom_for(iterable, func):
    it = iter(iterable)

    while True:
        try:
            func(next(it))
        except StopIteration:
            break

def cube(num):
    print(num ** 3)
custom_for([1,2,3,4,5], cube)
