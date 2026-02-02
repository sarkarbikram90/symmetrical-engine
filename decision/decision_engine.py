

from enum import Enum

class Decision(Enum):
    NO_ACTION = 0
    AUTO_HEAL = 1
    HITL_REQUIRED = 2

def decide_action(prediction: int) -> Decision:
    return Decision(prediction)
