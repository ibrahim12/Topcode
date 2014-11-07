
class IdentifyingWood:


  def check(self, s, t):

    n1 = len(s)
    n2 = len(t)

    success = "Yep, it's wood."
    failure = "Nope."

    if n2 > n1:
      return failure

    if n1 == n2 and s != t:
      return failure

    s_end_index = n1 - n2 + 1

    # for index_start in xrange(s_end_index):
    current = 0 
    for index_s in xrange(n1):

      if s[index_s] == t[current]:
        current += 1

      if current == n2:
        return success
          
    return failure


s = IdentifyingWood()

print s.check("abcd",'abce')
print s.check("absdefgh",'asdf')
print s.check("oxoxoxox",'ooxxoo')
