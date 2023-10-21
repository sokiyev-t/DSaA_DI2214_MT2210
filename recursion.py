
def fact(val):
    if val>1:
        return fact(val-1)*val
    else:
        return 1
# print(fact(5))

def countdown(n):
    print(n)
    if n<=0:
        return
    countdown(n-1);
countdown(5)
