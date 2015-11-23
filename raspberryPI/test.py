import sys
import location
import objectList
import config
from subprocess import Popen, PIPE

trackObject = int(sys.argv[1])

print location.siteLat
print("Tracking:")
print(trackObject)
print(objectList.spaceObjects[trackObject])


process = Popen(["/home/pi/Astro/libnova-0.15.0/examples/pointer_mars", "config.siteLat", "config.siteLon"], stdout=PIPE)
(output, err) = process.communicate()
print(output)
exit_code = process.wait()
