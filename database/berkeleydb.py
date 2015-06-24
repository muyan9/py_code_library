import bsddb

dbenv = bsddb.db.DBEnv()
file_path = "/root"
dbenv.open(file_path, bsddb.db.DB_CREATE |bsddb.db.DB_INIT_MPOOL)
db = bsddb.db.DB(dbenv)
filename = file_path + '/'+ 'recipient_bcc_maps.db'
db.open(filename, bsddb.db.DB_BTREE, bsddb.db.DB_RDONLY, 0660)

print db.get('test_key1')
print db.get('test_key2')

cur=db.cursor()
cur.set_range(prefix+'metadatatag')

firstTag = cur.next()

db.close()
dbenv.close()

