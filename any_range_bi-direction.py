# bi-directional moving stimulus at any given range

from psychopy import visual, core, event, monitors
import math

'USER INPUT HERE'
times = 5                # how many times do you want to present the same stimulus
direction ='2'      # right or left, moving direction of dots, '2' stands for 2 direction
distance = 0.5 # cm, distance between the screen and larvae's head
diameter = 3 # degree, size of visual stimulus in terms of visual angle
h_ratio = 0.7
w_ratio = 1.6
speed = 45               # degrees per second
range_start = -85
# where the stimulus starts
range_end = 85           # where the stimulus ends, value of end should always be bigger than start
x_halfangle = 85         # degrees, moving distance from left to centre in terms of visual angle, which takes 1/4 of total time
moving_y_angle = 0       # degree, correction for moving trace in terms of vertical direction

# elevation = 0            # degrees
# direction = 1            # TODO modify the direction of moving stimulus

'PARAMETERS SPECIFICALLY FOR MOVING TRACE CORRECTION'
monitor_width = 31                            # cm
monitor_size = [1280,720]                     # pixel
moving_time = (range_end-range_start)*2/float(speed)             # second
print moving_time
moving_y_speed = float(moving_y_angle*2/moving_time)     # degree per second
position = [range_start,-moving_y_angle]           # degree, initial position


'SET MONITOR PARAMETETRS'
myMonitor = monitors.Monitor('X1_carbon',width = 31 ,distance = distance)
myMonitor.setSizePix(monitor_size)
myMonitor.saveMon()

'CREATE A WINDOW'
myWin = visual.Window(monitor_size, monitor=myMonitor, units='deg', color = (-1,-1,-1), fullscr=True)
# units when setting the Window actually means nothing, I think.

'''get the the average time per frame'''
frametime = myWin.getMsPerFrame(nFrames=60, showVisual=False, msg='', msDelay=0.0)[0]
# return the the average time per frame, with unit of ms
deg_per_frame = frametime*speed/1000
y_deg_per_frame = frametime*moving_y_speed/1000

'CREATE A STIMULUS'
myStim = visual.Polygon(win=myWin, edges=100, size = [diameter/w_ratio, diameter/h_ratio], units='deg', lineColor=[1.0,1,1], fillColor=[1.0,1,1], pos=position)
# Create some coordinate stimulus
myCentre = visual.Polygon(win=myWin, edges=100, radius = diameter, units='degFlat', lineColor=[1, 1, 1], fillColor=[1, 1, 1], pos=[0,0])
leftmidEnd = visual.Polygon(win=myWin, edges=100, radius=diameter, units='degFlat', lineColor=[1, 1, 0], fillColor=[1, 1, 0], pos=[-60,-moving_y_angle])
rightmidEnd = visual.Polygon(win=myWin, edges=100, radius=diameter, units='degFlat', lineColor=[1, 1, 0], fillColor=[1, 1, 0], pos=[60,-moving_y_angle])
leftEnd = visual.Polygon(win=myWin, edges=100, radius=diameter, units='degFlat', lineColor=[1, 1, 0], fillColor=[1, 1, 0], pos=[-85,-moving_y_angle])
rightEnd = visual.Polygon(win=myWin, edges=100, radius=diameter, units='degFlat', lineColor=[1, 1, 0], fillColor=[1, 1, 0], pos=[85,-moving_y_angle])

'DISPLAY THE STIMULUS'
timer = core.Clock()  # create a clock to record the moving duration
#myCentre.draw()
myStim.draw()
#leftEnd.draw()
#rightEnd.draw()
myWin.update()

'START MOVING'
k_1 = event.waitKeys()
timer.reset()

for i in range(times):

    #following 5 lines are cali code, should be delete when running
    '''myCentre.draw()
    leftmidEnd.draw()
    rightmidEnd.draw()
    leftEnd.draw()
    rightEnd.draw()'''


    'Bi-directional moving in any given range'
    if direction == '2':
        while position[0] <= range_end:
            position[0] += deg_per_frame
            myStim.setPos(position)
            myStim.draw()
            myWin.update()
        while position[0] >= range_start:
            position[0] -= deg_per_frame
            myStim.setPos(position)
            myStim.draw()
            myWin.update()

    elif direction == 'right':
        while position[0]<= x_halfangle:
            position[0] += deg_per_frame
            position[1] += y_deg_per_frame #for correct the moving trace
            myStim.setPos(position)
            myStim.draw()
            myWin.update()
        position = [range_start,-moving_y_angle]
    else:
        while position[0]>= -x_halfangle:
            position[0] -= deg_per_frame
            position[1] += y_deg_per_frame #for correct the moving trace
            myStim.setPos(position)
            myStim.draw()
            myWin.update()



timeUse = timer.getTime() # unit (s)


print k_1, timeUse

'QUIT THE PROGRAM'
myWin.close()
core.quit()


