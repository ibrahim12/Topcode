from os.path import dirname
from top_code.lib import *
import os
from top_code.base import Settings
Settings['base_path'] = dirname(os.path.abspath(__file__))
print(Settings['base_path'])

class TheExperimentDiv2:


    def determineHumidity(self, intensity, L, leftEnd):

        int_list = list(intensity)
        result = []
        for val in leftEnd:

            intensity_value = 0
            total = val + L

            for index in range(val,total):
                intensity_value += int_list[index]
                int_list[index] = 0

            result.append( intensity_value )


        return result



s = TheExperimentDiv2()
# Submit(s.determineHumidity)

output = [0]*5
output[0] = s.determineHumidity([3, 4, 1, 1, 5, 6], 3, [3, 1, 0])
# output[1] = s.determineHumidity([20,8,6], 10, 15)
# output[2] = s.determineHumidity([10,20,30], 1, 18)
# output[3] = s.determineHumidity([100,200,301], 200, 200)

print(output)