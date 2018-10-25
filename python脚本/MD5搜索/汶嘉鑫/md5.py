#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
def md5(str):

    m = hashlib.md5()
    m.update(str.encode(encoding='utf-8'))
    #m.update(str)
    return m.hexdigest()
dmfile = open('TOP1000.txt')
dm = dmfile.read().splitlines()
#dm= ''.join(dm).strip('\n')
md5file = open('md5mima.txt','a+')
for d in dm:
    print (md5(d))
    md5file.write(d+'\t\t'+md5(d))
    md5file.write('\n')
dmfile.close()
md5file.close()



