import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:80")

words = server.sayHello("ss")

print "result:", words