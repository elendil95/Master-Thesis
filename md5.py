import os.path
import hashlib

home = os.path.expanduser("~")
target = home+"/Desktop/passwords.txt"
out=home+"/Desktop/out.txt"
#print(target)

with open(target) as f:
    with open(out, 'x') as o:
        for line in f:
            md5=hashlib.md5(line.encode('utf-8')).hexdigest()
            o.write(md5+"\n")
    o.close()
f.close()
