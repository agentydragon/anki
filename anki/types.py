from typing import Any, Dict, List, Tuple, Union

# Model attributes are stored in a dict keyed by strings. This type alias
# provides more descriptive function signatures than just 'Dict[str, Any]'
# for methods that operate on models.
# TODO: Use https://www.python.org/dev/peps/pep-0589/ when available in
# supported Python versions.

NoteType = Dict[str, Any]

Field = Dict[str, Any]

Template = Dict[str, Union[str, int, None]]

# Deck.
# Keys:
#    newToday: List[int] (currentDay, count)
#    revToday: List[int] (currentDay, count)
#    lrnToday: List[int] (currentDay, count)
#    timeToday: List[int]
#    conf: int
#    usn: int
#    desc: str
#    dyn: Union[int, bool]
#    collapsed: bool
#    extendNew: int
#    extendRev: int
Deck = Dict[str, Any]

# Deck configuration.
DeckConfig = Dict[str, Any]

QAData = Tuple[
    # Card ID this QA comes from. Corresponds to 'cid' column.
    int,
    # Note ID this QA comes from. Corresponds to 'nid' column.
    int,
    # ID of the model (i.e., NoteType) for this QA's note. Corresponds to 'mid' column.
    int,
    # Deck ID. Corresponds to 'did' column.
    int,
    # Index of the card template (within the NoteType) this QA was built
    # from. Corresponds to 'ord' column.
    int,
    # Tags, separated by space. Corresponds to 'tags' column.
    str,
    # Corresponds to 'flds' column. TODO: document.
    str,
    # Corresponds to 'cardFlags' column. TODO: document
    int,
]

TemplateRequirementType = str  # Union["all", "any", "none"]
# template ordinal, type, list of field ordinals
TemplateRequiredFieldOrds = Tuple[int, TemplateRequirementType, List[int]]
AllTemplateReqs = List[TemplateRequiredFieldOrds]
