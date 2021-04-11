from random import randint, shuffle

tpl = ["%(c)d+( )=%(mx)d", "( )+%(mn)d=%(mx)d", "%(c)d+%(mn)d=( )",
       "%(mx)d-( )=%(c)d", "( )-%(mn)d=%(c)d", "%(mx)d-%(mn)d=( )"]


# 不进/退位
def gen1(fmt):
    a = randint(0, 19)
    b = randint(0, a % 10)
    c = a - b
    if a == max(b,c):
        return gen1(fmt)
    l = [b, c]
    shuffle(l)
    n = {"mx":a, "mn":l[0], "c":l[1]}
    shuffle(fmt)
    return fmt[0] % n


# 进/退位
def gen2(fmt):
    n = {}
    a = randint(11, 18)
    b = randint((a % 10) + 1, 10)
    c = a - b
    if a == max(b,c):
        return gen1(fmt)
    l = [b, c]
    shuffle(l)
    n = {"mx":a, "mn":l[0], "c":l[1]}
    shuffle(fmt)
    return fmt[0] % n


add_fmt1 = ["%(c)d + %(mn)d = (  )"]
add_fmt2 = ["(  ) - %(mn)d = %(c)d"]
add_fmt3 = add_fmt1 + add_fmt2

div_fmt1 = ["%(mx)d - %(mn)d = (  )"]
div_fmt2 = ["%(mx)d - (  ) = %(mn)d", "%(mn)d + (  ) = %(mx)d", "(  ) + %(mn)d = %(mx)d"]
div_fmt3 = div_fmt1 + div_fmt2
for i in range(20):
    print("#".join([gen2(div_fmt1),
              gen2(div_fmt2),
              gen2(div_fmt3),
              gen2(div_fmt3)]))
