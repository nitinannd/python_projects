#What will the following script output? Please try to do this by mind if you can.
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())
#in this program we are assigning 2 inside a function that is not global function will treat 2 as the value of c
#if we want to print c=3 then we have to call print(c) instead of function (foo)