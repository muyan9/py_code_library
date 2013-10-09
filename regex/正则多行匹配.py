# -*- coding: cp936 -*-
##  多行匹配

##filecontent = '''
##	pattern
##	"(.*)(\\xE9\\x1C"
##	"\\xAD\\x6E"
##	"\\x00\\xFE"
##	"\\x03\\xFF................)(.*)$";
##
##	mapping (key,key);
##'''

import re


xxx = file(r"shellcode-signatures.sc",'r')
filecontent = xxx.read()
pattern='pattern.*";'
p = re.compile(pattern,re.DOTALL)
a=p.findall(filecontent)
print len(a)