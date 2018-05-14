#!/usr/bin/python

import hashlib
import itertools

#given hash from ./android/data/system/gesture.key
#2c 34 22 d3 3f b9 dd 9c de 87 65 74 08 e4 8f 4e 63 57 13 cb

charset = "012345678"
hashtofind = "2c3422d33fb9dd9cde87657408e48f4e635713cb"
for passlen in range(1,10):
  print "pass len tested is %d" %passlen
  for k in itertools.permutations(charset, passlen):
    strpass = "".join([chr(ord(item)-48) for item in k])
    h = hashlib.new('sha1')
    h.update(strpass)
    if h.hexdigest().upper().find(hashtofind.upper()) == 0:
      print "found for %s" % ''.join(k) 
      exit(-1)