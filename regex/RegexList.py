#!/usr/bin/env python
# -*- coding: cp936 -*-
def CreatRegexList():
    import re 
    
    filecontent=file('shellcode-signatures.sc','r');
    
    line1 = re.compile('pattern$')
    line2 = re.compile('".+"$')
    line3 = re.compile('".+";$')
    
    t = '';
    list_regex = [];
    i = 0;
    for a in filecontent.readlines():
        
        a = a.strip()
        if line1.match(a):
            t='';
        elif line2.match(a):
            aa=line2.match(a)
            t=t+aa.group()[1:-1]
        elif line3.match(a):
            aa=line3.match(a)
            t=t+aa.group()[1:-2]
            list_regex.append(t)
            
        
    return list_regex
