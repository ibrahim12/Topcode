class RectangleCoveringEasy:

  def sovle(self,holeH, holeW, boardH, boardW):

    if holeH > holeW:
      holeH, holeW = holwW, holeH

    elif holeH <= boardH and holeW <= boardW:
      return -1

    elif holeH <= boardW and holeW <= boardH:
      return -1

    else: 
      return 1
