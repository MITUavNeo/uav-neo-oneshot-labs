"""Module 5 Part 4 — Step 3: Detect Maze Exit and Land

The maze exit is detected when the front LIDAR distance exceeds EXIT_DISTANCE —
the drone has entered the open area beyond the final corridor wall.

Your task:
    Phase 0: Fly forward. When front >= EXIT_DISTANCE → stop, print, _phase = 1.
    Phase 1: Fly forward 1.5 more seconds past the threshold, then _done = True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as rc_utils

EXIT_DISTANCE = 4.0   # m — front clear beyond this = we've exited the maze
FLY_SPEED     = 0.35
FRONT_ANGLE   = 0; WINDOW = 15; MAX_RANGE = 10.0

_phase = 0; _timer = 0.0; _done = False

def reset():
    global _phase, _timer, _done
    _phase = 0; _timer = 0.0; _done = False

def update(drone):
    global _phase, _timer, _done
    if _done: return True

    s = drone.lidar.get_samples()
    front = min(rc_utils.get_lidar_average_distance(s, FRONT_ANGLE, WINDOW), MAX_RANGE)

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # if front >= EXIT_DISTANCE → stop, print, _phase = 1, _timer = 0.0
        # else → drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # fly forward 1.5 more seconds, then stop, print complete, _done = True

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
