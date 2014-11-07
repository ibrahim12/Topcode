
class GameOfStones:

  def count(self, stones):
    
    n = len(stones)
    if n == 1:
      return 1

    total = sum(stones)
    
    div,mod = divmod(total, n)
    
    if mod:
      return -1;

    for value in stones:
      div1, mod1 = divmod(abs(div-value), 2)
      
      if mod1:
        return -1

    return 1

s = GameOfStones()
print s.count([10,16])
print s.count([13,15,17,19,17])
print s.count([7,15,9,5])
print s.count([17])
print s.count([10, 15, 20, 12, 1, 20])