import itertools

#set = [11, 144, 44, 143, 9, 171, 54, 89, 62, 90, 216, 27, 179, 125, 161, 197]
#set = [81, 119, 221, 261, 39, 65, 53, 197, 67, 222, 91, 117, 260, 234, 208]
set = [432, 256, 17, 548, 480, 336, 224, 452, 128, 404, 208, 384, 49, 160, 352, 272]

for i in xrange(len(set)):
  for c in itertools.combinations(set, i):
    if sum(c) == 1000:
      print c
