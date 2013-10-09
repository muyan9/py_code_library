#!/usr/bin/env python
# -*- coding: cp936 -*-

#    import binascii
#    str_hex = binascii.b2a_hex(str_hex)

import RegexList,HexList,re,glob
list_regex = RegexList.CreatRegexList()

##store signatures compile of regex
list_regex_compiler = []

##write in list with compile of regex
try:
    i = 0
    for strregex in list_regex:
        i = i  + 1
        
        p = re.compile(strregex[1],re.IGNORECASE)
        list_regex_compiler.append([strregex[0],p])
except :
    print 'Error: Line%d %s' % (i,strregex)
    
#print 'match start ______________________'

file_match_result = file(r'match_result.txt','w')

filelist = glob.glob(r'F:\uuuuuu\aaa\*.*')
for t_file in filelist:
    filecontent = file(t_file)
    str_hex = filecontent.read()
    
    i = 0
    for p in list_regex_compiler:
        i = i + 1
        match_result = p[1].match(str_hex)
        if match_result:
            
#            print p[0]
#            print match_result.group()
#            print filecontent.name
            #sort
            file_match_result.write(p[0])
            #which file
            file_match_result.write('文件\r\n%s\r\n' % filecontent.name)
            #the part of match
            file_match_result.write('符合部分\r\n%s\n\n\n' % match_result.group())
            
    else:
        i = 0
else:
    file_match_result.close()
#    print 'match finished ______________________'
