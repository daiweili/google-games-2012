string = 'fgcagddc'

print string

def nextchr(char):
  ans = ord(char)+1
  if ans == ord('z'):
    ans = ord('a')
  return str(unichr(ans))

for i in xrange(26):
  print string
  string = map(nextchr, string)
