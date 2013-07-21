import hashlib
from uuid import getnode as get_mac

a = hashlib.sha512('felipe'+str(get_mac())).hexdigest()
f = open('.s.pa', 'wb')
f.write(a)
f.close()
