import sys
import math
import time
import subprocess

#This will be where the tracking happens.
#load location information
execfile('location.py')

# Object list
execfile('objectList.py')

#arguments passed from main.
trackObject = int(sys.argv[1])

if(trackObject == 0):
    print("Track Object 0")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','0'])
elif(trackObject == 1):
    print("Track Object 1")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','1'])
elif(trackObject == 2):
    print("Track Object 2")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','2'])
elif(trackObject == 3):
    print("Track Object 3")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','3'])
elif(trackObject == 4):
    print("Track Object 4")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','4'])
elif(trackObject == 5):
    print("Track Object 5")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','5'])
elif(trackObject == 6):
    print("Track Object 6")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','6'])
elif(trackObject == 7):
    print("Track Object 7")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','7'])
elif(trackObject == 8):
    print("Track Object 8")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','8'])
elif(trackObject == 9):
    print("Track Object 9")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','9'])
elif(trackObject == 10):
    print("Track Object 10")
    subprocess.Popen(['sudo','killall','startTrack.py'])
    subprocess.Popen(['python','startTrack.py','10'])
elif(trackObject == 11):
    print("Shutting down")
    execfile('shutdown.py')


#debug info
print("Tracking:")
print(trackObject)
print(spaceObjects[trackObject])
print("Site Lat Rad:")
print(siteLatRad)
print("Site Long Rad:")
print(siteLonRad)
print(spaceObjects[0])
