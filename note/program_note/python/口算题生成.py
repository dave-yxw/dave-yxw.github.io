from random import randint

tpl = ["%(c)d+( )=%(mx)d", "( )+%(mn)d=%(mx)d", "%(c)d+%(mn)d=( )",
       "%(mx)d-( )=%(c)d", "( )-%(mn)d=%(c)d", "%(mx)d-%(mn)d=( )"]


for i in range(20):
    l = []
    for c in range(5):
        n = {}
        a = randint(0, 19)
        b = randint(0, 19)
        n['mx'] = mx = max(a,b)
        n['mn'] = mn = min(a,b)
        n['c'] = mx - mn
        l.append(tpl[randint(0,5)] % n)
    print("#".join(l))