import locale
locale.getpreferredencoding()


ibrow = "مسعود"
ename="Masud"
aa=ibrow.encode("utf-8")
xx=ename.encode("utf-8")
va = aa==xx
print(va)
bb=aa.decode("utf-8")
print (aa)
print (xx)
print(bb)


u"✓ means check".encode("utf-8").decode("utf-8")
