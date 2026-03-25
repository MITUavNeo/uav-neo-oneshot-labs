"""Final Challenge 3 — Distance Maze (Right-Hand Rule)
Navigate an unknown maze using the right-hand-rule algorithm:

    1. If right side is open  (right > RIGHT_OPEN_THRES) → turn right (CW  = cur − 90°)
    2. Else if wall ahead     (front ≤ STOP_DISTANCE)    → turn left  (CCW = cur + 90°)
    3. Else                                              → fly forward

After each turn (Phase 1), advance briefly for 0.8 s (Phase 2) so sensors
clear the corner before re-evaluating.

Safety: stop after MAX_TURNS turns and return True.

Your task:
    Implement reset() and update() below.
    (Same algorithm as Module 5 Part 4.)
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '../../../../../../uav-neo-library/library'))
sys.path.insert(0, os.path.join(_HERE, '../../../../../library'))
import drone_core
import drone_utils as rc_utils

STOP_DISTANCE    = 1.2    # m — stop flying when this close to a wall
RIGHT_OPEN_THRES = 4.5    # m — right side "open" if distance > this value
FLY_SPEED        = 0.35
YAW_SPEED        = 0.5
YAW_THRESH       = 3.0
FRONT_ANGLE      = 0; RIGHT_ANGLE = 270; WINDOW = 15; MAX_RANGE = 10.0
MAX_TURNS        = 50     # safety: declare done after this many turns

# _phase: 0=fly/decide, 1=turning, 2=post-turn advance
_phase       = 0
_turn_count  = 0
_target_yaw  = 0.0
_nudge_timer = 0.0
_done        = False


def reset():
    global _phase, _turn_count, _target_yaw, _nudge_timer, _done
    ##################################
    #### START PUT CODE HERE #########

    # YOUR CODE HERE
    # Reset all state variables

    ###### END PUT CODE HERE #########
    ##################################
    pass


def _get(drone):
    s = drone.lidar.get_samples()
    f = min(rc_utils.get_lidar_average_distance(s, FRONT_ANGLE, WINDOW), MAX_RANGE)
    r = min(rc_utils.get_lidar_average_distance(s, RIGHT_ANGLE,  WINDOW), MAX_RANGE)
    return f, r


def _yaw_err(t, c):
    return ((t - c) + 180) % 360 - 180


def update(drone):
    """
    Apply right-hand-rule every frame.
    Returns True when MAX_TURNS is reached (maze exit).

    Hints (Phase 0 — fly/decide):
        front, right = _get(drone)
        if right > RIGHT_OPEN_THRES:
            stop; cur = attitude[1] % 360
            _target_yaw = (cur - 90) % 360   # turn right (CW)
            _turn_count += 1; _phase = 1
        elif front <= STOP_DISTANCE:
            stop; if _turn_count >= MAX_TURNS → _done = True
            _target_yaw = (cur + 90) % 360   # turn left (CCW)
            _turn_count += 1; _phase = 1
        else:
            drone.flight.send_pcmd(FLY_SPEED, 0, 0, 0)

    Hints (Phase 1 — yaw turn):
        err = _yaw_err(_target_yaw, cur)
        if |err| < YAW_THRESH → stop, _phase = 2
        else → yaw PCMD: send_pcmd(0, 0, clamp(err/45, -YAW_SPEED, YAW_SPEED), 0)

    Hints (Phase 2 — post-turn advance 0.8 s):
        send_pcmd(FLY_SPEED, 0, 0, 0)
        _nudge_timer += dt
        if _nudge_timer >= 0.8 → _phase = 0
    """
    global _phase, _turn_count, _target_yaw, _nudge_timer, _done
    if _done:
        return True

    if _phase == 0:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 1:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    elif _phase == 2:
        ##################################
        #### START PUT CODE HERE #########

        # YOUR CODE HERE

        ###### END PUT CODE HERE #########
        ##################################
        pass

    return _done
