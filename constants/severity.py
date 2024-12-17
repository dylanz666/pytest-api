from enum import Enum, unique


@unique
class Severity(Enum):
    # Blocker defect (functionality not implemented, cannot proceed to the next step)
    BLOCKER = "blocker"
    # Critical defect (missing functionality)
    CRITICAL = "critical"
    # Normal defect (boundary case, format error)
    NORMAL = "normal"
    # Minor defect (interface error not conforming to UI requirements)
    MINOR = "minor"
    # Trivial defect (mandatory items without prompts, or prompts are not standardized)
    TRIVIAL = "trivial"
