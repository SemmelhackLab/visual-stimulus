# stimulus moving in an up side down

from psychopy import visual, core, event, monitors
import math

'USER INPUT HERE'
times = 5                # how many times do you want to present the same stimulus
direction = '2'      # right or left, moving direction of dots, '2' stands for 2 direction
distance = 0.1           # cm, distance between the screen and larvae's head
diameter = 0.01          # degree, size of visual stimulus in terms of visual angle
h_ratio = 0.6
w_ratio = 1.5
speed = 40               # degrees per second
y_up = 20         # where the stimulus starts, up should always be positive
y_down = -20           # where the stimulus ends, end should always be negative or at least smaller than up
x_location = 60         # degrees, moving distance from left to centre in terms of visual angle, which takes 1/4 of total time

# elevation = 0            # degrees
# direction = 1            # TODO modify the direction of moving stimulus

'PARAMETERS SPECIFICALLY FOR MOVING TRACE CORRECTION'
monitor_width = 31                            # cm
monitor_size = [1280,720]                     # pixel
moving_time = (y_up-y_down)*2/float(speed)             # second
print moving_time
moving_y_speed = float((y_up-y_down)*2/moving_time)     # degree per second
position = [x_location,y_up]           # degree, initial position


'SET MONITOR PARAMETETRS'
myMonitor = monitors.Monitor('X1_carbon',width = 31 ,distance = distance)
myMonitor.setSizePix(monitor_size)
myMonitor.saveMon()

'CREATE A WINDOW'
myWin = visual.Window(monitor_size, monitor=myMonitor, units='degFlat', color = (-1,-1,-1), fullscr=True)
# units when setting the Window actually means nothing, I think.

'''get the the average time per frame'''
frametime = myWin.getMsPerFrame(nFrames=60, showVisual=False, msg='', msDelay=0.0)[0]
# return the the average time per frame, with unit of ms
deg_per_frame = frametime*speed/1000
y_deg_per_frame = frametime*moving_y_speed/1000

'CREATE A STIMULUS'
myStim = visual.Polygon(win=myWin, edges=100, size = [diameter/w_ratio, diameter/h_ratio], units='degFlat', lineColor=[1, 1, 1], fillColor=[1, 1, 1], pos=position)


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

    'Bi-directional moving in any given range'
    if direction == '2':
        while position[1] >= y_down:
            position[1] -= deg_per_frame
            myStim.setPos(position)
            myStim.draw()
            myWin.update()
        while position[1] <= y_up:
            position[1] += deg_per_frame
            myStim.setPos(position)
            myStim.draw()
            myWin.update()



timeUse = timer.getTime() # unit (s)


print k_1, timeUse

'QUIT THE PROGRAM'
myWin.close()
core.quit()


