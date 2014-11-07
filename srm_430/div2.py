from os.path import dirname
from top_code.lib import *
import os
from top_code.base import Settings
Settings['base_path'] = dirname(os.path.abspath(__file__))
print(Settings['base_path'])

class CreateGroups:

    def minChanges(self, groups, minSize, maxSize):
        if maxSize > maxSize :
            return -1

        n = len(groups)
        total = sum(groups)
        dis = total // n

        # print(dis, minSize, maxSize, total, dis * n)

        if dis * n == total:
            if dis < minSize or dis > maxSize:
                return -1
        else:
            import math
            if math.ceil(total / n) >= maxSize:
                return -1

            if math.floor(total / n ) <= minSize:
                return -1


        result = 0
        needed = 0
        for val in groups:

            if val < minSize:
                result += ( minSize - val )
                needed += ( minSize - val )

            if val > maxSize:
                needed -= ( val - maxSize )


        if needed < 0:
            result += -needed

        return result



s = CreateGroups()
# Submit(s.minChanges)

output = [0]*5
output[0] = s.minChanges([10,20],10,15)
output[1] = s.minChanges([20,8,6], 10, 15)
output[2] = s.minChanges([10,20,30], 1, 18)
output[3] = s.minChanges([100,200,301], 200, 200)



print(output)