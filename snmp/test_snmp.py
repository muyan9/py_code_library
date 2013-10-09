'''
Created on May 31, 2013

@author: zcy
'''
import netsnmp


oid = netsnmp.Varbind('laLoad.1')
result = netsnmp.snmpwalk(oid,
                         Version = 1,
                         DestHost="localhost",
                         Community="public")

# result = netsnmp.snmpwalk(oid,
#                                 Version = 2,
#                                 DestHost="localhost",
#                                 Community="public")

print result