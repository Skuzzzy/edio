import codecs
f = codecs.open('edict2', encoding='euc-jp')
for line in f:
    print(repr(line))