kwargs = ["A", "B", "C", "D", "E", "F"]
args = ["X", "Y"]

def args_in_kwargs(args, kwargs):
    for arg in args:
        if arg in kwargs:
            return True
    return False

my_list = [x**2 for x in range(100) if x%2==0]
print(my_list)
print(args_in_kwargs(args=args, kwargs=kwargs))