"""Module 5 Part 3 — Step 3: Detect Left Opening
Fly forward until the left LIDAR distance exceeds half the corridor width,
indicating an opening. Then turn left and fly to the next wall.

Your task:
    Phase 0 (scan + fly):
        Read front and left LIDAR. Fly forward (FLY_SPEED).
        opening_threshold = _corridor_width * OPENING_FACTOR
        If left > opening_threshold → stop, print, _phase = 1, _nudge_timer = 0.
        If front <= STOP_DISTANCE → stop, print error, _done = True.
    Phase 1 (nudge forward 1.0s):
        Send forward PCMD. _nudge_timer += dt.
        After 1.0s → compute _target_yaw = (cur + 90) % 360 (CCW = left), _phase = 2.
    Phase 2 (turn left):
        Yaw to _target_yaw. When aligned → stop, _phase = 3.
    Phase 3 (fly to next wall):
        Fly forward until front <= STOP_DISTANCE → stop, print, _done = True.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as rc_utils

STOP_DISTANCE   = 1.2
OPENING_FACTOR  = 1.5   # left_dist > corridor_width * factor → opening found
FLY_SPEED       = 0.35
YAW_SPEED       = 0.5; YAW_THRESH = 3.0
FRONT_ANGLE=0; LEFT_ANGLE=90; RIGHT_ANGLE=270; WINDOW=15; MAX_RANGE=10.0

_phase = 0; _corridor_width = 3.0; _target_yaw = 0.0; _nudge_timer = 0.0; _done = False

def reset(corridor_width=3.0):
    global _phase, _corridor_width, _target_yaw, _nudge_timer, _done
    _phase = 0; _corridor_width = corridor_width
    _target_yaw = 0.0; _nudge_timer = 0.0; _done = False

def _get(drone):
    s = drone.lidar.get_samples()
    f = min(rc_utils.get_lidar_average_distance(s, FRONT_ANGLE, WINDOW), MAX_RANGE)
    l = min(rc_utils.get_lidar_average_distance(s, LEFT_ANGLE,  WINDOW), MAX_RANGE)
    return f, l

def _yaw_err(t, c): return ((t-c)+180)%360-180

def update(drone):
    global _phase, _target_yaw, _nudge_timer, _done
    if _done: return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # front, left = _get(drone)
        # opening_threshold = _corridor_width * OPENING_FACTOR
        # if left > opening_threshold:
        #     stop, print opening found, _phase = 1, _nudge_timer = 0.0
        # elif front <= STOP_DISTANCE:
        #     stop, print hit wall, _done = True
        # else:
        #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Nudge forward: drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)
        # _nudge_timer += drone.get_delta_time()
        # After 1.0s → cur = drone.physics.get_attitude()[1] % 360
        #              _target_yaw = (cur + 90) % 360  (CCW = left)
        #              _phase = 2

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Yaw to _target_yaw (same pattern as step2_navigate)
        # When aligned → stop, _phase = 3

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 3:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Read front LIDAR. If front <= STOP_DISTANCE → stop, print complete, _done = True
        # Else → fly forward

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
