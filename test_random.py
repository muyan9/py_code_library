import random

def random_int(min=0, max=0):
    if min>max:
        t = max
        max = min
        min = t
    return random.randint(min, max)

def random_textstring(len, lrange=0, rrange=0):
    ret = ""
    for i in range(len+random_int(0-lrange, rrange)):
        ret = "%s%s" % (ret, chr(random_int(32,126)))
    return ret
 
def random_binstring(len, lrange=0, rrange=0):
    ret = ""
    for i in range(len+random_int(0-lrange, rrange)):
        ret = "%s%s" % (ret, chr(random_int(0,127)))
    return ret


if __name__ == "__main__":
    for i in range(10):
        a= random_binstring(10)
        print len(a), a
