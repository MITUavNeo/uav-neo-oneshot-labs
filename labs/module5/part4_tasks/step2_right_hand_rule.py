"""Module 5 Part 4 — Step 2: Right-Hand Rule Maze Solver

Algorithm — runs every frame in Phase 0:
    1. If right > RIGHT_OPEN_THRES  → turn right (CW = cur - 90°)
    2. Else if front <= STOP_DISTANCE → turn left  (CCW = cur + 90°)
    3. Else → fly forward

Phase 1: Execute yaw turn to _target_yaw.
Phase 2: Advance briefly (0.8s) after turn before re-evaluating.
Safety: stop after MAX_TURNS turns.

Your task:
    Implement the three phases described above.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../library'))
import drone_core, drone_utils as rc_utils

STOP_DISTANCE    = 1.2    # m — stop flying forward at this distance from wall
RIGHT_OPEN_THRES = 4.5    # m — right side is "open" if > this value
FLY_SPEED        = 0.35
YAW_SPEED        = 0.5; YAW_THRESH = 3.0
FRONT_ANGLE = 0; LEFT_ANGLE = 90; RIGHT_ANGLE = 270; WINDOW = 15; MAX_RANGE = 10.0
MAX_TURNS = 30            # safety: give up after this many turns

_phase      = 0   # 0=fly_fwd, 1=turn, 2=post_turn_advance
_turn_count = 0
_target_yaw = 0.0
_nudge_timer = 0.0
_done       = False

def reset():
    global _phase, _turn_count, _target_yaw, _nudge_timer, _done
    _phase = 0; _turn_count = 0; _target_yaw = 0.0; _nudge_timer = 0.0; _done = False

def _get(drone):
    s = drone.lidar.get_samples()
    f = min(rc_utils.get_lidar_average_distance(s, FRONT_ANGLE, WINDOW), MAX_RANGE)
    r = min(rc_utils.get_lidar_average_distance(s, RIGHT_ANGLE,  WINDOW), MAX_RANGE)
    return f, r

def _yaw_err(t, c): return ((t - c) + 180) % 360 - 180

def update(drone):
    global _phase, _turn_count, _target_yaw, _nudge_timer, _done
    if _done: return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # front, right = _get(drone)
        # if right > RIGHT_OPEN_THRES:
        #     stop; cur = attitude[1] % 360
        #     _target_yaw = (cur - 90) % 360  # CW = subtract
        #     _turn_count += 1; print; _phase = 1; _nudge_timer = 0.0
        # elif front <= STOP_DISTANCE:
        #     stop; if _turn_count >= MAX_TURNS → done
        #     _target_yaw = (cur + 90) % 360  # CCW = add (turn left)
        #     _turn_count += 1; print; _phase = 1; _nudge_timer = 0.0
        # else:
        #     drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # err = _yaw_err(_target_yaw, drone.physics.get_attitude()[1] % 360)
        # if |err| < YAW_THRESH → stop; _nudge_timer = 0.0; _phase = 2
        # else → yaw PCMD

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE
        # Fly forward briefly (0.8s) so sensors clear the corner, then _phase = 0

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
