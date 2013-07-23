import hashlib
from uuid import getnode as get_mac

SAL = 'validade12'

a = hashlib.sha512('felipe'+SAL+str(get_mac())).hexdigest()
f = open('.s.pa', 'wb')
f.write(a)
f.close()
