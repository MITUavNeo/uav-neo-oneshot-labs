"""Module 5 Part 1 — Step 2: Read Distance Sensors
Use the LIDAR to measure wall distances in three directions.

LIDAR angle convention:
    0°   = straight ahead (forward)
    90°  = left
    270° = right

Your task:
    1. Hover: drone.flight.stop()
    2. Get LIDAR samples: samples = drone.lidar.get_samples()
    3. Read front, left, right distances using rc_utils.get_lidar_average_distance(samples, angle, WINDOW).
       Clamp each reading to MAX_RANGE.
    4. Estimate corridor_width = left_dist + right_dist.
    5. Print a summary, set _done = True, return True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as rc_utils

# LIDAR averaging windows (degrees)
FRONT_ANGLE = 0;   LEFT_ANGLE = 90;   RIGHT_ANGLE = 270
WINDOW      = 15   # ± degrees to average around each direction
MAX_RANGE   = 10.0 # metres — clamp readings

# Exported values (read by other steps after update() returns True)
front_dist = 0.0
left_dist  = 0.0
right_dist = 0.0
corridor_width = 0.0

_done = False

def reset():
    global _done
    _done = False

def update(drone):
    global front_dist, left_dist, right_dist, corridor_width, _done
    if _done: return True

    drone.flight.stop()   # hover while reading

    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # samples = drone.lidar.get_samples()
    # front_dist = min(rc_utils.get_lidar_average_distance(samples, FRONT_ANGLE, WINDOW), MAX_RANGE)
    # left_dist  = min(rc_utils.get_lidar_average_distance(samples, LEFT_ANGLE,  WINDOW), MAX_RANGE)
    # right_dist = min(rc_utils.get_lidar_average_distance(samples, RIGHT_ANGLE, WINDOW), MAX_RANGE)
    # corridor_width = left_dist + right_dist
    # print results, set _done = True

    ###### END PUT CODE HERE #########
    ##################################

    return _done
