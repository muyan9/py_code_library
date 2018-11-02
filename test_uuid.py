import uuid

print uuid.uuid1()
print uuid.uuid4()
print uuid.NAMESPACE_DNS
print uuid.NAMESPACE_OID
print uuid.NAMESPACE_URL
print uuid.NAMESPACE_X500
print uuid.uuid3(uuid.NAMESPACE_DNS,"b")
print uuid.uuid5(uuid.NAMESPACE_DNS,"b")