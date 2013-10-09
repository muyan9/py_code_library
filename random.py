import random

datacount = 1000000


def random_str(str_length = 100 , lrange = 97 , rrange = 122):
    str = ""
    for i in range(random.randint(1,str_length)):
        str = str + chr(random.randint(lrange, rrange))
        #str = str + chr(random.randint(33,126))
    return str


f = open('testdata.txt','w')
f.write('%s\n' % random_str(5))
f.write('\t%s\n' % random_str(5))
for i in range(datacount):
    f.write('%s%s\n' % (random.randint(1,2)*'\t',random_str(100)))

f.close()