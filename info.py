#
# Fetching System Information with Python
# Author -  MC.Naveen
# Tested with Python3 on Elementary OS Juno 5.0 (Based on Ubuntu 18.04)
# 

import platform
import time,sys

animation = "|/-\\"

for i in range(5):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\nHere you go..\n")
time.sleep(1)
# Architecture

print('Architecture:' + platform.architecture()[0])

# machine
print('Machine:' + platform.machine())

# node
print("System Name: " + platform.node())

print("\n##################\n")

# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

print("\n##################\n")    

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)
print("\n##################\n")    
# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")