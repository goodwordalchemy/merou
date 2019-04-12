from enum import Enum
from typing import NamedTuple


class GroupJoinPolicy(Enum):
    CAN_JOIN = "canjoin"
    CAN_ASK = "canask"
    NOBODY = "nobody"


Group = NamedTuple("Group", [("name", str), ("description", str), ("can_join", GroupJoinPolicy)])


class GroupNotFoundException(Exception):
    """Attempt to operate on a group not found in the storage layer."""

    def __init__(self, name):
        # type: (str) -> None
        msg = "Group {} not found".format(name)
        super(GroupNotFoundException, self).__init__(msg)
