import zipfile

path = '/home/zcy/test/a.zip'
a = zipfile.ZipFile(path)

b = a.namelist()
print b[0].decode('gbk')
print a.printdir()