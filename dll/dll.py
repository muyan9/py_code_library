import ctypes
dll = ctypes.windll.LoadLibrary( 'SetFileParser.dll' )
print dir(dll)
print dll._name
print dll._FuncPtr(0)