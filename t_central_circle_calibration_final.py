# NOTE. Create a white circle in the centre for calibration (red-point display the center of screen)
# NOTE. MANUAL FOR USING
# STEP-1. display the circle with diamter, measure the projected width and height, calculated the corresponding w_ratio and h_ratio (ratio = projected/displayed) and fill in the INPUT PART
# STEP-2. display the circle, measure the projected width and height to make sure the calibration is accurate

from psychopy import visual, core, event, monitors
import math

'USER INPUT HERE'
distance = 1.0

# cm, distance between the screen and larvae's head
diameter = 40            # degree, size of visual stimulus in terms of visual angle
h_ratio = 0.7            # ratio = projected/displayed
w_ratio = 1.6            # ratio = projected/displayed

'SET MONITOR PARAMETETRS'
monitor_width = 31                            # cm
monitor_size = [1280,720]                     # pixel
myMonitor = monitors.Monitor('X1_carbon',width = 31 ,distance = distance)
myMonitor.setSizePix(monitor_size)
myMonitor.saveMon()

'CREATE A WINDOW'
myWin = visual.Window(monitor_size, monitor=myMonitor, units='degFlat', color = (-1,-1,-1), fullscr=True)

'CREATE A STIMULUS'
myCentre = visual.Polygon(win=myWin, edges=100, size = (diameter/w_ratio, diameter/h_ratio), units='degFlat', lineColor=[1, 1, 1], fillColor=[1, 1, 1], pos=[0,0])
myCentrePoint = visual.Polygon(win=myWin, edges=100, radius = 1, units='degFlat', lineColor=[1, 0, 0], fillColor=[1, 0, 0], pos=[0,0])

'DISPLAY THE STIMULUS'
timer = core.Clock()  # create a clock to record the moving duration
myCentre.draw()
myCentrePoint.draw()
myWin.update()

k_1 = event.waitKeys()

'QUIT THE PROGRAM'
myWin.close()
core.quit()


