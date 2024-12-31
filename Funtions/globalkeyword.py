a = 10
b = 17
print(id(b))


def something():
    global a  # it will be same global variable so change affect
    a = 14
    print("in fun ", a)
    b = 10  #local variable 'b'
    x = globals()['b']  # function globals() have all global variable
    # above we are extracting b
    print(id(b))
    # changing global variable 'b' value
    globals()['b'] = 11
    print('local b ', b)


something()
print("outside ", a)
print('outside b : ', b)