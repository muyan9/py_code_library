import SimpleXMLRPCServer

class MyObject:
    def sayHello(self, s):
        return "hello xmlprc " + s

obj = MyObject()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 80))
server.register_instance(obj)

print "Listening on port 80"
server.serve_forever()