# enter the distance(mm), diameter in terms of degree and return a diameter in terms of mm

import math

# INPUT HERE
distance = 4 # mm
diameter = 0.5 # degFlat

diameter = diameter*math.pi/180 # transfer to arc

diameter = 2*(distance*math.tan(diameter/2))
print 'diameter should be ', diameter, 'mm.'
