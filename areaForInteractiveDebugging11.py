#import areaForInteractiveDebugging
#import pdb
#areaForInteractiveDebugging.crash()
#pdb.pm()

def areaOfTriangle():

 base = 10
 height = 5
 area = 1/2 * (base * height )
 print("Area of our triangle is : ", area)

import pdb
pdb.set_trace()
areaOfTriangle()