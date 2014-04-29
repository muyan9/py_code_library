import os, time, sys, random
import requests

s_pre = sys.argv[1]

f_log = open('%s.log' % s_pre, 'a')

t_data_4k = ''
for i in range(1024 * 4):
	t_data_4k += chr(random.randint(1,254))

index = 0
url = 'http://10.255.193.225:8341/upload'
for i in range(20 * 10000):
	t_blocks = random.randint(32, 51)#128K-20M
	content = t_data_4k * t_blocks
	files = {'uploadedfile': ('a%s' % index, content)}
	r = requests.post(url, files=files)
	if 'OK' in r.text:
		index+=1
		f_log.write('a%s\t%s\n' % (index, len(content)/1024))
f_log.close()